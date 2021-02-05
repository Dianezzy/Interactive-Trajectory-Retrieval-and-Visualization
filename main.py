# import os
# os.environ["OMP_NUM_THREADS"] = "1"
#
# import subprocess
# from multiprocessing.pool import Pool
# import glob
# import json
# #from dtw_dist import *
# from LCSS import *
# #from edit_dist import edit_dist
# #from frechetdist import frdist
# from SAX import  *
# from utils import *
# CHOSEN_INDEX = [1,10,20,30,40]
# import time
# COLLATED_DATA_DIR = "data/collated_data/trajectory"
# def process(metric, test_file_path):
#     #p = Pool(os.cpu_count())
#     fn = glob.glob(COLLATED_DATA_DIR + "/*/*/*/*")
#     if metric == 'LCSS':
#         true_prediction = 0
#         test_cnt = 0
#         #lcss_start = time.time()
#         #res = LCSS(test_file_path, fn, CHOSEN_INDEX)
#         for cid in CHOSEN_INDEX:
#             LCSS(test_file_path, fn, cid)
#         #lcss_end = time.time()
#         #print('lcss time cost', lcss_end - lcss_start, 's')
#         #print(lcss2tag)
#             lst = sorted(lcss2tag.items(), key = lambda item:item[0], reverse=True)
#         # for simi in res:
#             # if(res in lcss2tag.keys()):
#             #     print(lcss2tag[res])
#             res = (lst[:10])
#             start = cid * STEP
#             end = start + WINDOW_SIZE
#             for x in res:
#                 print(x)
#             #print("1",test_file_path.split("/")[-1]+"_"+str(start)+"_"+str(end))
#             for x in res:
#                 if test_file_path.split("/")[-1]+"_"+str(start)+"_"+str(end) in x[1]:
#                     print([start, end])
#                     true_prediction += 1
#             test_cnt += 1
#         print("enen",[test_cnt, true_prediction])
#
#
#
#
#
# if __name__ == '__main__':
#     #player2trajectory("data/test/31/movement_31.json", 203138)
#     process('LCSS','data/collated_data/trajectory/0021500023/31/home/p_203138')
#
import os
os.environ["OMP_NUM_THREADS"] = "1"
true_prediction = 0
test_cnt = 0
import subprocess
from multiprocessing.pool import Pool
import glob
import json
#from dtw_dist import *
from LCSS import *
#from edit_dist import edit_dist
#from frechetdist import frdist
from SAX import  *
from utils import *
CHOSEN_INDEX = [1,10,20,30,40]
import time
COLLATED_DATA_DIR = "data/collated_data/trajectory"
def process(metric, test_file_path):
    global true_prediction
    global test_cnt
    #p = Pool(os.cpu_count())
    fn = glob.glob(COLLATED_DATA_DIR + "/*/*/*/*")
    if metric == 'LCSS':
        #lcss_start = time.time()
        #res = LCSS(test_file_path, fn, CHOSEN_INDEX)
        for cid in CHOSEN_INDEX:
            LCSS(test_file_path, fn, cid)
        #lcss_end = time.time()
        #print('lcss time cost', lcss_end - lcss_start, 's')
        #print(lcss2tag)
            lst = sorted(lcss2tag.items(), key = lambda item:item[0], reverse=True)
        # for simi in res:
            # if(res in lcss2tag.keys()):
            #     print(lcss2tag[res])
            res = (lst[:30])
            start = cid * STEP
            end = start + WINDOW_SIZE
#             for x in res:
#                 print(x)

            print("1",test_file_path.split("/")[-1]+"_"+str(start)+"_"+str(end))
            precision = 0
            for x in res:

                if test_file_path.split("/")[-1]+"_"+str(start)+"_"+str(end) in x[1]:
                    #print([start, end])

                    true_prediction += 1
                    break
            test_cnt += 1
        print("enen",[test_cnt, true_prediction])

    if metric == 'EDIT':
        # lcss_start = time.time()
        # res = LCSS(test_file_path, fn, CHOSEN_INDEX)
        for cid in CHOSEN_INDEX:
            (test_file_path, fn, cid)
            # lcss_end = time.time()
            # print('lcss time cost', lcss_end - lcss_start, 's')
            # print(lcss2tag)
            lst = sorted(lcss2tag.items(), key=lambda item: item[0], reverse=True)
            # for simi in res:
            # if(res in lcss2tag.keys()):
            #     print(lcss2tag[res])
            res = (lst[:30])
            start = cid * STEP
            end = start + WINDOW_SIZE
            #             for x in res:
            #                 print(x)

            print("1", test_file_path.split("/")[-1] + "_" + str(start) + "_" + str(end))
            precision = 0
            for x in res:

                if test_file_path.split("/")[-1] + "_" + str(start) + "_" + str(end) in x[1]:
                    # print([start, end])

                    true_prediction += 1
                    break
            test_cnt += 1
        print("enen", [test_cnt, true_prediction])





if __name__ == '__main__':
    #player2trajectory("data/test/31/movement_31.json", 203138)
    # process('LCSS','data/collated_data/trajectory/0021500010/1/home/p_2772')
    # process('LCSS','data/collated_data/trajectory/0021500010/1/home/p_201951')
    # process('LCSS','data/collated_data/trajectory/0021500010/1/home/p_203093')
    # process('LCSS','data/collated_data/trajectory/0021500010/1/home/p_201935')
    # process('LCSS','data/collated_data/trajectory/0021500010/1/home/p_203991')
    process('LCSS', 'data/collated_data/trajectory/0021500023/31/home/p_203138')