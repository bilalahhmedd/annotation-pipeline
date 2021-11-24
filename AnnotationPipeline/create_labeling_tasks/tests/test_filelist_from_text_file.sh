SCRIPT=`realpath $0`
SCRIPTDIR=`dirname $SCRIPT`
PYDIR=`dirname $SCRIPTDIR`
python $SCRIPTDIR/dump_filelist_to_text_file.py --images-folder some_shoes/ --fnames-to-dump-to available_images0.txt available_images1.txt --image-counts-per-fname 4

python3 $PYDIR/divide_images_with_json.py  \
--filelist-file available_images0.txt available_images1.txt --n-annotators 4 --n-repetition 3 \
--annotators-root-folder tasks_for_annotators  --annotator-prefix annotator \
 --container-document-root / \
 --container-images-folder /label-studio/data/some_shoes
