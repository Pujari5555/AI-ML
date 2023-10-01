clc;
close all;
clear all;

% Define the directory containing the input images
inputDir = 'C:\Users\one\OneDrive\Documents\MATLAB\Examples\R2022b\matlab\ReadVideoFiles28781487Example\';

% Create a cell array to store the input image filenames
inputImageFiles = cell(1, 8);

% Load the input images and process each one
for i = 1:8
    % Construct the filename for the input image
    inputImageFiles{i} = fullfile(inputDir, sprintf('Img_00%d.png', i));
    
    % Load the input image
    inputImage = imread(inputImageFiles{i});
    
    % Convert to grayscale
    grayInputImage = rgb2gray(inputImage);
    
    % Apply contrast stretching
    contrastStretchedImage = imadjust(grayInputImage);
    
    % Apply adaptive histogram equalization
    enhancedImage = adapthisteq(contrastStretchedImage);
    
    % Load the pre-trained denoising network
    %net = denoisingNetwork('DnCNN');
    
    % Denoise the enhanced image
    loadedNet = load('denoisingModel3.mat');
    net = loadedNet.net;
    denoisedImage = denoiseImage(enhancedImage, net);
    % Create subplots for each image
    subplot(3, 8, i);
    imshow(grayInputImage);
    title(sprintf('Original %d', i));
    
    subplot(3, 8, i + 8);
    imshow(enhancedImage);
    title(sprintf('Enhanced %d', i));
    
    subplot(3, 8, i + 16);
    imshow(denoisedImage);
    title(sprintf('Denoised %d', i));
end

% Adjust the subplot layout for all subplots
ax = gca;
ax.Position(3) = 0.2;  % Adjust the width of the subplots

% Set the figure title
suptitle('Image Enhancement and Denoising');
