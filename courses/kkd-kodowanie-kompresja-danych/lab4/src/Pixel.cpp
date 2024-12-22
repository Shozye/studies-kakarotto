#include "Pixel.h"

Pixel::Pixel(){
    Pixel(0,0,0);
}    
Pixel::Pixel(int blue, int green, int red){
    this->b = blue;
    this->g = green;
    this->r = red;
};
