from argparse import ArgumentParser
import os
from collections import defaultdict
import json
def test_oversampled(annotator_root_folder,
                    annotator_prefix):
    n_annotators = len(
        [annotator_folder for annotator_folder in os.listdir(annotator_root_folder) if annotator_folder.startswith(f'{annotator_prefix}_')]
    )
    file_counters = defaultdict(int)
    for ann_i in range(n_annotators):
        annotator_folder = os.path.join(annotator_root_folder,f'{annotator_prefix}_{ann_i}')
        for json_fname in os.listdir(annotator_folder):
            full_json_fname = os.path.join(annotator_folder,json_fname)
            with open(full_json_fname,'r') as f:
                loaded = json.load(f)
            file_counters[loaded['data']] = file_counters[loaded['data']] + 1
    print(file_counters)
    print(file_counters.values())
    pass
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--annotator-root-folder',type=str)
    parser.add_argument('--annotator-prefix',type=str)
    args = parser.parse_args()
    test_oversampled(args.annotator_root_folder,
                    args.annotator_prefix)