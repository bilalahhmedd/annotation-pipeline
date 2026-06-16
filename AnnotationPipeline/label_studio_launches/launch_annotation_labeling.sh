# 
SCRIPTPATH=`realpath $0`
SCRIPTDIR=`dirname $SCRIPTPATH`
n_annotators=50
n_repetition=5
annotator_prefix="annotator"
container_name="label_studio_annotator_container"
path_to_app="/home/user/color_annotation_app_2"

server_folder_on_host=$path_to_app"/server-folder"
images_folder_on_host="$SCRIPTDIR/../Images"
_1_level_above_images_folder_on_host="$(dirname "$images_folder_on_host")"
basename_of_images_folder_on_host="$(basename "$images_folder_on_host")"
root_folder_for_annotator_jsons_on_host=$path_to_app"/label_studio_tasks/tasks_for_color_annotation"
basename_of_root_folder_for_annotator_jsons_on_host="$(basename "$root_folder_for_annotator_jsons_on_host")"
folder_for_annotation_results=$path_to_app"/label_studio_annotation_results/annotated_colors"
_1_level_above_folder_for_annotation_results="$(dirname "$folder_for_annotation_results")"
basename_of_folder_for_annotation_results="$(basename "$folder_for_annotation_results")"
folder_on_container_for_annotation_results="/label-studio/$basename_of_folder_for_annotation_results"
data_folder_on_container="/label-studio/data"
labelstudio_document_root="/"
labeling_config="$SCRIPTDIR/../label_studio_labeling_configs/color_annotation_labeling_config.yml"

# port on docker container
target_port=8080
# post on host
host_port=8083

# echo $n_annotators
# echo $annotator_prefix
# echo $container_name
# echo $images_folder_on_host
# echo $_1_level_above_images_folder_on_host
# echo $basename_of_images_folder_on_host
# echo $root_folder_for_annotator_jsons_on_host
# echo $basename_of_root_folder_for_annotator_jsons_on_host
# echo $folder_for_annotation_results
# echo $folder_on_container_for_annotation_results
# echo $data_folder_on_container
# echo $labelstudio_document_root
# echo $labeling_config
# echo $target_port
# echo $host_port

# exit 0 

docker stop $container_name
docker rm $container_name

# python3 $SCRIPTDIR/../create_labeling_tasks/divide_images_with_json.py  --actual-images-folder $images_folder_on_host --n-annotators $n_annotators --annotators-root-folder $root_folder_for_annotator_jsons_on_host --annotator-prefix $annotator_prefix --container-document-root $labelstudio_document_root --container-images-folder $data_folder_on_container/$basename_of_images_folder_on_host
mkdir $server_folder_on_host
python3 $SCRIPTDIR/../create_labeling_tasks/divide_images_with_json.py  \
--actual-images-folder $images_folder_on_host --n-annotators $n_annotators  --n-repetition $n_repetition \
--annotators-root-folder $root_folder_for_annotator_jsons_on_host  --annotator-prefix $annotator_prefix \
 --container-document-root $labelstudio_document_root \
 --container-images-folder $data_folder_on_container/$basename_of_images_folder_on_host

python3 $SCRIPTDIR/../create_labeling_tasks/create_folders_for_annotation_export.py \
	--export-folder $folder_for_annotation_results --n-annotators $n_annotators \
	--annotator-prefix $annotator_prefix

cp -rf "${root_folder_for_annotator_jsons_on_host}/annotator_0" "${root_folder_for_annotator_jsons_on_host}/demo"
mkdir "${folder_for_annotation_results}/demo"


docker run -d -p $host_port:$target_port -v $images_folder_on_host:$data_folder_on_container/$basename_of_images_folder_on_host -v $server_folder_on_host:$data_folder_on_container -v $root_folder_for_annotator_jsons_on_host:/label-studio/$basename_of_root_folder_for_annotator_jsons_on_host -v $folder_for_annotation_results:$folder_on_container_for_annotation_results --env LOCAL_FILES_SERVING_ENABLED=true --env LOCAL_FILES_DOCUMENT_ROOT=/ --name $container_name heartexlabs/label-studio:latest label-studio

echo 'docker done'

docker cp $labeling_config $container_name:/label-studio/label_studio/annotation_templates/computer-vision


