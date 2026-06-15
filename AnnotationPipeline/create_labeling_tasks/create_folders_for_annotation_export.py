import argparse
import os
def create_folders_for_annotation_export(export_folder, n_annotators,annotator_prefix,purge=True):
	""" creates folders a per number of annotator using annotator prefixes to serve data to label-studio app

	Args:
		export_folder (_str_): _folder path where data will be exported_
		n_annotators (_int_): _number of folder to create for each annotator_
		annotator_prefix (_str_): _string to be added to name of annotator project_
		purge (bool, optional): _description_. Defaults to True.
	"""
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