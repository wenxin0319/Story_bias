from allennlp.predictors.predictor import Predictor
import allennlp_models.coref
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python script.py input_file output_folder")
        return

    f_name = sys.argv[1]
    output_folder = sys.argv[2]

    f = open(f_name, "r")
    txt = [line.strip() for line in f.readlines() if line.strip()]
    print(f"Total paragraphs: {len(txt)}")
    print(f"First paragraph: {txt[0]}")

    predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2020.02.27.tar.gz", cuda_device=0)
    predictor._model = predictor._model.cuda()
    print(f"CUDA device: {predictor.cuda_device}")
    print("Predictor loaded")

    male_pronouns = {"he", "him"}
    female_pronouns = {"she", "her"}

    def get_pronouns(para):
        pron = []
        pron_pos = []
        output = predictor.predict(document=para)

        if output['clusters']:
            cluster_len = [len(i) for i in output['clusters']]
            for tup in output['clusters'][cluster_len.index(max(cluster_len))]:
                s = tup[0]
                t = tup[1]
                if s == t:
                    pron_pos.append((s, s))
                else:
                    pron_pos.append((s, t + 1))
                pron.append(" ".join(output['document'][s:t + 1]))
        else:
            return None, None

        return pron, pron_pos

    cnt = 0
    for para in txt:
        try:
            pronouns, pronoun_positions = get_pronouns(para)
            if pronouns is None or not pronouns:
                continue

            pronouns = set(map(str.lower, pronouns))
            if pronouns & male_pronouns and not (pronouns & female_pronouns):
                output_file = f"{output_folder}/male.txt"
            elif pronouns & female_pronouns and not (pronouns & male_pronouns):
                output_file = f"{output_folder}/female.txt"
            else:
                output_file = f"{output_folder}/unresolved.txt"

            with open(output_file, 'a') as f:
                f.write(f"{para}\n")

            cnt += 1
            if cnt % 100 == 0:
                print(f"Processed {cnt} paragraphs")
        except:
            continue


if __name__ == '__main__':
    main()
