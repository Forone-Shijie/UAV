import cv2

capture = cv2.VideoCapture("/data/sjzhang/UAV/dataset/UAV_video/dynamic_marker/dynamic_marker_calibration_1_tracking.mp4")
dst = 0
i=2000

if capture.isOpened() is True:
    while(True):
        ret, frame = capture.read()
        cv2.imwrite('/data/sjzhang/UAV/dataset/UAV_video/dynamic_marker/Img/img' + str(i) + '.png', frame)
        i += 1
        print(i)

delta = []
ground_truth = [1.5, 1.8, 2.1, 2.4, 2.7, 3.0, 3.3, 4.9, 5.2, 5.5, 5.8, 6.1, 6.4, 6.7, 7.0, 7.3]
calculated_location = [1.497425457, 1.779649801, 2.10202869, 2.381167379, 2.454566297, 3.017524423, 3.33692034, 4.861911988,
                       5.151847031, 5.508523624, 5.808962343, 6.116225856, 6.428043132, 6.720896511, 7.008048785, 7.371827785]
index = 0
flag = [0 for i in range(len(ground_truth))]
color = ['green' for i in range(len(ground_truth))]
print(color)

#除去坏点的版本
for each_i, each_j in zip(ground_truth, calculated_location):
        print("{}, {}".format(each_i, each_j))
        if abs(each_i - each_j) < 0.1:
            delta.append(abs(each_i - each_j))
        else:
            print('{}'.format(index))
            flag[index] = 1
        index += 1

print(flag)
#除去坏点的版本
i = 0
for each_flag in flag:
    if each_flag == 1:
        del ground_truth[i]
        del calculated_location[i]
    i += 1


# #保留坏点的版本
# for each_i, each_j in zip(ground_truth, calculated_location):
#     delta.append(abs(each_i - each_j))
#     print("{}, {}".format(each_i, each_j))
#     if abs(each_i - each_j) >= 0.1:
#         print(abs(each_i- each_j))
#         color[index] = 'red'
#     index += 1
#
# #保留坏点的版本
# for each_i, each_j in zip(ground_truth, calculated_location):
#     print("{}, {}".format(each_i, each_j))
#     if abs(each_i - each_j) >= 0.1:
#         print(abs(each_i- each_j))
#         color[index] = 'red'
#     index += 1

print(color)
print(delta)


import numpy as np
import matplotlib.pyplot as plt

def draw_bar(labels, quants):
    width = 0.4
    ind = np.linspace(0.5, 15.5, len(labels))
    # make a square figure
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    # Bar Plot
    ax.bar(ind - width / 2, quants, width, color=color)
    # Set the ticks on x-axis
    ax.set_xticks(ind)
    ax.set_xticklabels(labels)
    # labels
    ax.set_xlabel('Ground_Truth /m',)
    ax.set_ylabel('Error /m')
    # title
    ax.set_title('Error analysis', bbox={'facecolor': '0.8', 'pad': 5})
    plt.grid(True)
    plt.show()
    plt.savefig("bar.jpg")
    plt.close()


labels = ['1.5', '1.8', '2.1', '2.4', '2.7', '3.0', '3.3', '4.9', '5.2', '5.5', '5.8', '6.1', '6.4', '6.7', '7.0', '7.3']
print(ground_truth)
draw_bar(list(map(str, ground_truth)), delta)
print(np.mean(delta))