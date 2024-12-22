#include"Pixel.h"
#include<cmath>
#include<string>

double entropy(Pixel* pixels, int width, int height, std::string type){
    int frequency[256] = {0};
    for(int row = 0; row < height; row++){
        for(int col = 0; col < width; col++){
            Pixel pixel = pixels[row*width + col];
            if (type == "blue"){
                frequency[pixel.b]++;
            }
            else if (type == "red"){
                frequency[pixel.r]++;
            }
            else if (type == "green"){
                frequency[pixel.g]++;
            }
            else{
                frequency[pixel.r]++;
                frequency[pixel.g]++;
                frequency[pixel.b]++;
            }
        }
    }
    double size;
    if (type == "blue" || type == "red" || type == "green")
        size = width*height;
    else
        size = width*height*3;
    double sum = 0;
    for( int i = 0; i < 256; i++){
        if (frequency[i] != 0){
            sum += frequency[i] * std::log2l(frequency[i]);
        }
    }
    return std::log2l(size) - (sum/(double)size);
}