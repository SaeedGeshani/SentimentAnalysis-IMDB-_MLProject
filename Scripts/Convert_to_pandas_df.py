import glob
import os
import pandas as pd

def txtfolder_to_contentlist(directory_path):

    print(f"Searching {directory_path} to find the contents.")

    file_paths = glob.glob(f"{directory_path}/*.txt")

    if not file_paths:
        print(f"There is not any txt formatted file in {directory_path}.")
        return []
    
    print(f"Starting to extract text of the folder {directory_path}.")

    file_contents = []

    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                file_contents.append(content)
        except UnicodeDecodeError:
            try:
                with open(file_path, 'r', 'latin1') as file:
                    content = file.read()
                    file_contents.append(content)
            except Exception as e:
                print(f"Exception has occured -> {e}.")
        except Exception as e:
            print(f"Exception has Occured -> {e}.")

    return file_contents



def make_dataframe_by_list(overviews, type):

    df = pd.DataFrame({'sentiment' : [1 if type=='pos' else 0 for _ in range(len(overviews))], 'overview' : [overview for overview in overviews]})

    return df


def extract(directory_path):

    pos_overviews = txtfolder_to_contentlist(f"{directory_path}/pos")
    neg_overviews = txtfolder_to_contentlist(f"{directory_path}/neg")

    df1 = make_dataframe_by_list(pos_overviews, 'pos')
    df2 = make_dataframe_by_list(neg_overviews, 'neg')
    df = pd.concat([df1, df2], ignore_index=True)

    return df



