SCRIPT=`realpath $0`
SCRIPTPATH=`dirname $SCRIPT`
PYPATH=`dirname $SCRIPTPATH`

python3 $PYPATH/divide_images_with_json.py  \
--actual-images-folder some_shoes --n-annotators 4 --n-repetition 3 \
--annotators-root-folder tasks_for_annotators  --annotator-prefix annotator \
 --container-document-root / \
 --container-images-folder /label-studio/data/some_shoes


python3 $SCRIPTPATH/test_oversampling.py  \
--annotator-root-folder tasks_for_annotators \
--annotator-prefix annotator
