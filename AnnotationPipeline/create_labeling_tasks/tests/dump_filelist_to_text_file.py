from argparse import ArgumentParser
import os
def dump_image_fnames_to_file(image_fnames,fname):
	with open(fname,'w') as f:
		for line in image_fnames:
			f.write(f'{line}\n')

if __name__ == '__main__':
	parser = ArgumentParser()
	parser.add_argument('--images-folder',type=str)
	parser.add_argument('--fnames-to-dump-to',type=str,nargs='+')
	parser.add_argument('--image-counts-per-fname',type=int,nargs='+')

	args = parser.parse_args()

	assert any([
		len(args.fnames_to_dump_to) == len(args.image_counts_per_fname),
		len(args.fnames_to_dump_to) == len(args.image_counts_per_fname) +1,
		])

	available_images = [os.path.join(args.images_folder,fname) for fname in os.listdir(args.images_folder)]
	total_available_images = len(available_images)
	if len(args.fnames_to_dump_to) == len(args.image_counts_per_fname) +1:
		args.image_counts_per_fname = args.image_counts_per_fname + [total_available_images - sum(args.image_counts_per_fname)]
	assert all([c>0 for c in args.image_counts_per_fname])
	remaining_images = available_images
	for fname,count in zip(args.fnames_to_dump_to,args.image_counts_per_fname):

		dump_image_fnames_to_file(remaining_images[:count],fname)
		remaining_images = remaining_images[count:]
