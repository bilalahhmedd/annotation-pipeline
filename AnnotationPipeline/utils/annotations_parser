import json
from tqdm import tqdm_notebook as tqdm
from collections import defaultdict
# from tqdm import tqdm as tqdm

def handle_attributes(ann,
    single_choice_attributes = ['department','closure','type','style'],
    multiple_choice_attributes = []
     ):
    '''
    this takes care of what attributes are supposed to be single-choice,
    which ones are multiple-choice etc
    '''
    for attr_name in ann:
        if attr_name in single_choice_attributes:
            ann[attr_name] = ann[attr_name][0]
            pass
        elif attr_name in multiple_choice_attributes:
            pass
    return ann

# {'department': ['womens shoes'],
#  'closure': ['pull-on/slip-on'],
#  'type': ['casual'],
#  'style': ['Slip-On']}            
            
def parse_single_json(fname,handle_attributes=lambda ann:ann):
    with open(fname,'r') as f:
        J = json.load(f)
#     import pdb;pdb.set_trace()
    was_cancelled = J['was_cancelled']
    is_labelled = J['task']['is_labeled']
    data = J['task']['data']['data']
    out = {}
    out['data'] = data
    if not was_cancelled and is_labelled:
        ann = J['result']
        for item in ann:
            attribute_name = item['from_name']
            value = item['value']
            if 'choices' in value:
                attribute_value = value['choices']
            out[attribute_name] = attribute_value
        pass
    
    out = handle_attributes(out)
    return out
#===================================================================================

import os


def read_all_annotators_data(
    annotation_results_folder,
    prefix_to_exclude_demo = 'annotator_'):

    annotator_folders = os.listdir(annotation_results_folder)
    annotator_folders = list(sorted(annotator_folders))
    all_annotations = []
    for person_i,annotator_folder in enumerate(tqdm(annotator_folders)):

        if not annotator_folder.startswith(prefix_to_exclude_demo):
            continue
        full_annotator_folder = os.path.join(annotation_results_folder,annotator_folder)
        fname_annotated_jsons = [fname for fname in os.listdir(full_annotator_folder) if fname.endswith('.json')]
        full_fname_annotated_jsons = [os.path.join(full_annotator_folder,fname) for fname in fname_annotated_jsons]
        annotated_by_this_annotator = []
        for jname in full_fname_annotated_jsons:
            ann = parse_single_json(jname,handle_attributes=handle_attributes)
            ann['json-fname'] = jname
            annotated_by_this_annotator.append(ann)
        all_annotations.append(annotated_by_this_annotator)
        '''
        if person_i == 5:
            # for debugging
            break
        '''
    return all_annotations
def keep_only_most_recent_annotation(annotations):
    imnames = [ann_i['data'] for ann_i in annotations]
#     import pdb;pdb.set_trace()
    indexes = range(len(imnames))
    imname_vs_index = defaultdict(list)
    for n,i in zip(imnames,indexes):
        imname_vs_index[n].append(i)
    indexes_to_keep = []
    for (imname,locs) in (imname_vs_index.items()):
        if len(locs) == 1:
            indexes_to_keep.append(locs[0])
        else:
            '''
            example time string: 2021-11-08T04:41:37.086182Z
            '''
            year = "0000"
            month = "11"
            day = "08"
            hour = "00"
            minute = "00"
            latest_loc = -1
            for li in locs:
                json_fname = annotations[li]['json-fname']
                
                with open(json_fname,'r') as f:
                    J = json.load(f)
                    J = J['updated_at']
                    J_year = J[:len(year)]
                    J_month = J[len(year + '-'):len(year + '-')+len(month)]
                    J_day = J[len(year + '-')+len(month + '-'):len(year + '-')+len(month + '-') + len(day)]
                    J_hour = J[len(year + '-')+len(month + '-') + len(day + 'T'):len(year + '-')+len(month + '-') + len(day + 'T') + len(hour)]
                    J_minute = J[len(year + '-')+len(month + '-') + len(day + 'T') + len(hour+":"):len(year + '-')+len(month + '-') + len(day + 'T') + len(hour+":")+len(minute)]
                    #..............................................
                    if int(year) > int(J_year):
#                         print(f'continuing from year {year},{J_year}')
                        continue
                    if (int(year) == int(J_year)):
                        if (int(month)> int(J_month)):
#                             print(f'continuing from month {month},{J_month}')
                            continue                          
                        if (int(month) == int(J_month)):
                            if (int(day) > int(J_day)):
#                                 print(f'continuing from day {day},{J_day}')
                                continue
                            if (int(day) == int(J_day)):
                                if (int(hour) > int(J_hour)):
#                                     print(f'continuing from hour {hour},{J_hour}')
                                    continue
                                if (int(hour) == int(J_hour)):
                                    if (int(minute) > int(J_minute)):
#                                         print(f'continuing from minute {minute},{J_minute}')
                                        continue
                    #..............................................
                    year = J_year
                    month = J_month
                    day = J_day
                    hour = J_hour
                    minute = J_minute
                    latest_loc = li
                    #..............................................
            assert latest_loc > -1
            indexes_to_keep.append(latest_loc)
#     indexes_to_keep = list(sorted(indexes_to_keep))
    '''
    indexes_to_drop = list(set(indexes).difference(indexes_to_keep))
    df_kep = df_annotations[df_annotations.iloc is in ]
    '''
    kept = [annotations[i]  for i in indexes_to_keep]
    return kept
                    

#     imname_counts = Counter(imnames)
    
#     types_of_counts = list(set(imname_counts.values()))
#     count_vs_observation = defaultdict(list)
#     for i,(a,c) in enumerate(imname_counts.items()):
#         count_vs_observation[c].append(dfi.iloc[i])
        
#     if max(types_of_counts) > 1:
#         import pdb;pdb.set_trace()           
        
#===================================================================================

import pandas as pd
from functools import reduce
from collections import Counter
import numpy as np


def outer_merge_annotations(annotations):  
    # will take per-annotator dataframes
    # and create a new data frame where
    # the closure choice of annotator 0 is closure_0
    # the closure choice of annotator 1 is closure_1
    # etc, and similarly for all other attributes
    
    df_merged = annotations[0].copy()
    for i,df_next in enumerate(annotations[1:]):
        df_merged = df_merged.merge(df_next,on='data',suffixes=(f'',f'_{i+1}'),how='outer')

    return df_merged
    pass

def aggregate_annotations(
    all_annotations,
    fields,
):
    '''
    to collect all annotators data, and 
    aggregate multiple annotations for 1 image
    '''

    all_annotations_non_empty = [ann for ann in all_annotations if len(ann) > 0]
    df_annotations = [pd.DataFrame.from_dict(ann) for ann in all_annotations_non_empty]
    #--------------------------------
    from collections import Counter,defaultdict
    
    #--------------------------------
    '''
    stop if any annotator has annotated the same image more than once
    this should have been addressed in an earlier step
    '''
    for dfi in df_annotations:   
        imnames = list(dfi.data)
        imname_locs = defaultdict(list)
        for i,n in enumerate(imnames):
            imname_locs[n].append(i)
        for n,locs in imname_locs.items():
            if len(locs) > 1:
                import pdb;pdb.set_trace()
    #--------------------------------
    df_annotations = outer_merge_annotations(df_annotations)
    print('annotations merged')
    print(f'#annotations {len(df_annotations)}')


    for k in tqdm(fields):
        # sometimes labelstudio inexplicably puts the selected option
        # inside a list example: instead of 'closure' being 'zip'
        # it'll be ['zip'].
        # this takes care of that

        #---------------------------------
        def strip_list(el):
            if isinstance(el,list):
                assert len(el) == 1
                return el[0] 
            else: 
                return el
        #---------------------------------
        for column in df_annotations.columns: 
            if column.startswith(k):


                df_annotations[column] = df_annotations[column].apply(
                    strip_list,
                    )



        # example:combine all closure columns into 1 column
        df_annotations[k] = df_annotations.apply(lambda row:[row[column] for column in row.keys() if column.startswith(k) and not pd.isna(row[column])] ,
                                                     axis=1)
        print(f'{k} columns combined')
        #example: count unique closure values in each row
        df_annotations[k] = df_annotations.apply(lambda row:Counter(row[k]),
                                                     axis=1)
        print(f'{k} values counted')
        # example: pick the closure value with highest count, given it is larger than 2
        # assumption: if lace-up/tie has count of 2 , all other closures will have counts <= 1
        df_annotations[k] = df_annotations.apply(lambda row: max(row[k],key=row[k].get) \
                                                 if  ( len(row[k]) > 0 and (max(row[k].values()) > 1) ) else float('nan'),\
                                                  axis=1)
        print(f'most common {k} value chosen')
        print('-'*40)

    df_annotations_columns = df_annotations.columns
    for column in df_annotations_columns:
        for k in fields:
            if column.startswith(f'{k}_'):
                print(column,end=' ')
                df_annotations = df_annotations.drop([column],axis=1)
    imnames = list(df_annotations.data)
    uq_imnames = set(imnames)
#     if len(uq_imnames) != len(imnames):
#         import pdb;pdb.set_trace()
    return df_annotations

def remove_tag_choices(df_annotations):
    '''
    will remove the tag-choices column from a data frame
    '''
    for column in df_annotations.columns:
        for k in ['tag-choices']:
            if column.startswith(f'{k}_'):
                print(column,end=' ')
                df_annotations = df_annotations.drop([column],axis=1)
    return df_annotations

