clear all;
clc;
srcDic = uigetdir('Z:\data\sjzhang\UAV\dataset\UAV_video\dynamic_marker\Img\');
cd(srcDic);
allnames = struct2cell(dir('*.png'));
[k,len]=size(allnames);
aviobj = VideoWriter('Z:\data\sjzhang\UAV\dataset\UAV_video\dynamic_marker\dynamic_marker_calibration_1.avi');
aviobj.FrameRate = 50;
open(aviobj)
for i = 1:len
    name = allnames{1,i};
        frame = imread(name);
        writeVideo(aviobj,frame);
end
close(aviobj)



