import argparse
import os
def create_folders_for_annotation_export(export_folder, n_annotators,annotator_prefix,purge=True):
	
	if purge:
		os.system(f"rm -rf {export_folder}")
	os.makedirs(export_folder)
	for ann_i in range(n_annotators):
		os.mkdir(
			os.path.join(export_folder,f"{annotator_prefix}_{ann_i}")
			)
	pass
if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('--export-folder',type=str)
	parser.add_argument('--n-annotators',type=int)
	parser.add_argument('--annotator-prefix',type=str)
	"""
	python3 create_folders_for_annotation_export.py \
	--export-folder annotated --n-annotators 3 \
	--annotator-prefix annotator
	"""
	args = parser.parse_args()
	create_folders_for_annotation_export(args.export_folder, args.n_annotators,args.annotator_prefix)