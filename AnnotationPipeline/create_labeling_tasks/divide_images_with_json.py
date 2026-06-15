import os
import numpy as np
import json
import argparse
from collections import defaultdict
#====================================
'''
def divide_images_with_repetition(images_folder,n_annotators,n_repetition=1,
    image_extensions =  ['.jpg','.jpeg','.png','.gif','.bmp']):
    assert n_repetition <= n_annotators, 'number of image repetition should be <= n_annotators'
    excluded_fnames = []
    im_fnames = [] 
    for fname in os.listdir(images_folder):
        if any([fname.lower().endswith(ext) for ext in image_extensions]):
            im_fnames.append(fname)
        else:
            excluded_fnames.append(fname)
    im_fnames = sorted(im_fnames)
    print(f'excluded fnames: {excluded_fnames[:10]}')
    counters_for_annotators = defaultdict(int)
    assigned_im_fnames = [[] for _ in range(n_annotators)]
    for i,im_fname in enumerate(im_fnames):
        annotators_for_im = np.random.choice(n_annotators,size = n_repetition,replace=False)
        for ann_i in annotators_for_im:
            assigned_im_fnames[ann_i].append(im_fname)
    return assigned_im_fnames

#====================================
def divide_images(images_folder,n_annotators,
    image_extensions =  ['.jpg','.jpeg','.png','.gif','.bmp']):

    excluded_fnames = []
    im_fnames = [] 
    for fname in os.listdir(images_folder):
        if any([fname.lower().endswith(ext) for ext in image_extensions]):
            im_fnames.append(fname)
        else:
            excluded_fnames.append(fname)
    im_fnames = sorted(im_fnames)
    print(f'excluded fnames: {excluded_fnames[:10]}')
    n_images = len(im_fnames)
    images_per_annotator = int(np.ceil(n_images/n_annotators))
    order = np.arange(n_images)
    order = np.random.permutation(order)
    assigned_ixs = []
    assigned_im_fnames = []
    for i_ann in range(n_annotators):
        assigned_ixs = order[i_ann*images_per_annotator:(i_ann+1)*images_per_annotator]
        # assigned_ixs.append(
        #   order[i_ann*images_per_annotator:(i_ann+1)*images_per_annotator]
        #   )
        assigned_im_fnames.append([im_fnames[i] for i in assigned_ixs])
        
    return assigned_im_fnames
'''

def get_available_fnames(
    images_folder = None,
    text_file_with_fnames = None,
    image_extensions = []
):
    """ get file names for given folder

    Args:
        images_folder (_string_, optional): _path to image folder_. Defaults to None.
        text_file_with_fnames (_type_, optional): _description_. Defaults to None.
        image_extensions (list, optional): _list of images extensions_. Defaults to [].

    Returns:
        _type_: _description_
    """
    if images_folder is not None:
        excluded_fnames = []
        im_fnames = [] 
        for fname in os.listdir(images_folder):
            if any([fname.lower().endswith(ext) for ext in image_extensions]):
                im_fnames.append(fname)
            else:
                excluded_fnames.append(fname)
        im_fnames = sorted(im_fnames)
        print(f'excluded fnames: {excluded_fnames[:10]}')            
        return im_fnames,excluded_fnames
    if text_file_with_fnames is not None:
        # print(text_file_with_fnames)
        excluded_fnames = []
        im_fnames = [] 
        with open(text_file_with_fnames,'r') as f:
            fnames = f.readlines()
        fnames = [fname.rstrip('\n') for fname in fnames]
        # print(fnames)
        for fname in fnames:
            if any([fname.lower().endswith(ext) for ext in image_extensions]):
                im_fnames.append(fname)
            else:
                excluded_fnames.append(fname)
        # assert False,'Not tested'
        return im_fnames,excluded_fnames


def divide_images_with_repetition(im_fnames,
    n_annotators,n_repetition=1,
    image_extensions =  ['.jpg','.jpeg','.png','.gif','.bmp']):
    """ divide images as per number of annotators and n number of copies of each image

    Args:
        im_fnames (_list_): _description_
        n_annotators (_any_): _description_
        n_repetition (int, optional): _description_. Defaults to 1.
        image_extensions (list, optional): _description_. Defaults to ['.jpg','.jpeg','.png','.gif','.bmp'].

    Returns:
        _type_: image folders created
    """
    assert n_repetition <= n_annotators, 'number of image repetition should be <= n_annotators'
    excluded_fnames = []
    assigned_im_fnames = [[] for _ in range(n_annotators)]
    # print(im_fnames,'\n','!!!!')
    for i,im_fname in enumerate(im_fnames):
        annotators_for_im = np.random.choice(n_annotators,size = n_repetition,replace=False)
        for ann_i in annotators_for_im:
            assigned_im_fnames[ann_i].append(im_fname)
    return assigned_im_fnames

def divide_images(im_fnames,
    n_annotators):
    """ divide images are per number of annotators

    Args:
        im_fnames (_any_): image file names
        n_annotators (_int_): number of annotators

    Returns:
        _type_: _description_
    """
    n_images = len(im_fnames)
    images_per_annotator = int(np.ceil(n_images/n_annotators))
    order = np.arange(n_images)
    order = np.random.permutation(order)
    assigned_ixs = []
    assigned_im_fnames = []
    for i_ann in range(n_annotators):
        assigned_ixs = order[i_ann*images_per_annotator:(i_ann+1)*images_per_annotator]
        # assigned_ixs.append(
        #   order[i_ann*images_per_annotator:(i_ann+1)*images_per_annotator]
        #   )
        assigned_im_fnames.append([im_fnames[i] for i in assigned_ixs])
    return assigned_im_fnames
def im_fname_to_labelstudio_json(folder,im_fname):
    return {
            "data": f"/data/local-files/?d={os.path.join(folder,im_fname)}"
            }
    pass
def purge_folder(folder):
    os.system(f'rm -rf {folder}')
    if not os.path.exists(folder):
        os.makedirs(folder)
    pass
def dump_divided_images_as_jsons(root_folder,annotator_prefix,assigned_im_fnames,
    container_document_root,container_images_folder,
    purge=True,
    counters_for_annotators = defaultdict(int)):
    """ dumps divided images as json files inside annotator folder. where each json contains path to image and annotation meta data

    Args:
        root_folder (_str_): _folder path where annotator folders to be created_
        annotator_prefix (_type_): _name prefix to be added each folder name_
        assigned_im_fnames (_type_): _list of file names_
        container_document_root (_type_): _docker container root folder path_
        container_images_folder (_type_): _label studion container images folder path_
        purge (bool, optional): _description_. Defaults to True.
        counters_for_annotators (_type_, optional): number of annotators.
    """

    if purge:
        purge_folder(root_folder)
    #------------------------------
    container_relative_path_of_images = os.path.relpath(container_images_folder,container_document_root)
    #------------------------------
    for i_ann,im_fnames_for_annotator in enumerate(assigned_im_fnames):
        annotator_folder = os.path.join(root_folder,annotator_prefix+f'_{i_ann}')
        if not os.path.exists(annotator_folder):
            os.mkdir(annotator_folder)
        for i_im,im_fname in enumerate(im_fnames_for_annotator):
            json_as_dict = im_fname_to_labelstudio_json(container_relative_path_of_images,im_fname)
            with open(os.path.join(annotator_folder,f'{ counters_for_annotators[i_ann]}.json'),'w') as f:
                json.dump(json_as_dict,f)
                counters_for_annotators[i_ann] = counters_for_annotators[i_ann] + 1
    pass

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--actual-images-folder',type=str)
    parser.add_argument('--filelist-file',type=str,nargs='+')
    parser.add_argument('--n-annotators',type=int)
    parser.add_argument('--n-repetition',default=1,type=int)
    parser.add_argument('--annotators-root-folder',type=str)
    parser.add_argument('--annotator-prefix',type=str)
    parser.add_argument('--container-document-root',type=str)
    parser.add_argument('--container-images-folder',type=str)
    args = parser.parse_args()
    '''
    python3 divide_images_with_json.py  --actual-images-folder some_shoes \
    --n-annotators 2 \
    --annotators-root-folder tasks_for_annotators --annotator-prefix annotator \
    --container-document-root / --container-images-folder /label-studio/data/some_shoes 
    '''
    # images_folder = 'some_shoes'
    # n_annotators = 2
    # root_folder = 'annotator-jsons'
    # annotator_prefix = 'annotator'
    # mounted_images_folder = images_folder
    if args.actual_images_folder is not None:
        available_im_fnames,_ = get_available_fnames(images_folder = args.actual_images_folder, 
            image_extensions =  ['.jpg','.jpeg','.png','.gif','.bmp'])
        assigned_im_fnames = divide_images_with_repetition(available_im_fnames,args.n_annotators,n_repetition=args.n_repetition)
        dump_divided_images_as_jsons(args.annotators_root_folder,args.annotator_prefix,assigned_im_fnames,
            args.container_document_root,args.container_images_folder,purge=True)
    elif args.filelist_file is not None:
        counters_for_annotators = defaultdict(int)
        purge_folder(args.annotators_root_folder)
        for filelist_file in args.filelist_file:
            available_im_fnames,_ = get_available_fnames(text_file_with_fnames = filelist_file, 
                image_extensions =  ['.jpg','.jpeg','.png','.gif','.bmp'])
            # print(available_im_fnames,'\n','^^^^^')
            assigned_im_fnames = divide_images_with_repetition(available_im_fnames,args.n_annotators,n_repetition=args.n_repetition)
            # print(assigned_im_fnames,'\n'+'-'*10)
            dump_divided_images_as_jsons(args.annotators_root_folder,args.annotator_prefix,assigned_im_fnames,
                args.container_document_root,args.container_images_folder,
                counters_for_annotators = counters_for_annotators,
                purge=False)
