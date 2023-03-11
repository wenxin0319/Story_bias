from comet2.comet_model import PretrainedCometModel
import pickle

comet_model = PretrainedCometModel(device=0)


def write_file(file_name, content):
    with open(file_name, 'a') as f:
        f.write(content)


def save_file(output_name, content):
    with open(output_name, 'wb') as f:
        pickle.dump(content, f)


def get_dict(file_name, mode):
    with open(file_name, "r") as f:
        text = [line[:512] for line in f.readlines() if line != " \n"]

    if mode == "xAttr":
        predictions = [comet_model.predict(st, "xAttr", num_beams=5) for st in text]
        save_file(file_name + "_at_dict", predictions)
    elif mode == "xReact":
        predictions = [comet_model.predict(st, "xReact", num_beams=5) for st in text]
        save_file(file_name + "_xr_dict", predictions)
    elif mode == "oReact":
        predictions = [comet_model.predict(st, "oReact", num_beams=5) for st in text]
        save_file(file_name + "_or_dict", predictions)
    elif mode == "motivation":
        wt_dict = []
        nd_dict = []
        it_dict = []

        for st in text:
            wt_inference = comet_model.predict(st, "xWant", num_beams=5)
            wt_dict.append(wt_inference[0])

            nd_inference = comet_model.predict(st, "xNeed", num_beams=5)
            nd_dict.append(nd_inference[0])

            it_inference = comet_model.predict(st, "xIntent", num_beams=5)
            it_dict.append(it_inference[0])

        save_file(file_name + "_wt_dict", wt_dict)
        save_file(file_name + "_nd_dict", nd_dict)
        save_file(file_name + "_it_dict", it_dict)


if __name__ == "__main__":
    file_names = ["result/female_masked_subj.txt", "result/female_two_and_above_subj.txt",
                  "result/female_two_and_above_obj.txt"]
    modes = ["xAttr", "xReact", "oReact"]

    for file_name in file_names:
        for mode in modes:
            get_dict(file_name, mode)
    
    file_names = ["result/male_masked_subj.txt", "result/male_two_and_above_subj.txt",
                  "result/male_two_and_above_obj.txt"]
    modes = ["xAttr", "xReact", "oReact"]

    for file_name in file_names:
        for mode in modes:
            get_dict(file_name, mode)

