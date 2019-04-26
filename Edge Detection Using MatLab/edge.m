srcFile = dir('D:\1\*.JPG');
for i=1:length(srcFile)
    filename = strcat('D:\1\',srcFile(i).name);
    I=imread(filename);
    J=rgb2gray(I);
    edges= edge(J,'Sobel');
    figure,imshow(edges);
    path = strcat('D:\1\2\',srcFile(i).name);
    imwrite(edges,path);
end