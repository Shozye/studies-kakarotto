#include<string>
#include"utils.cpp"
#include<stdio.h>
#include<cstring>
#include"Pixel.h"
#define BYTE_SIZE 256

enum Origin{
    BOTTOM_LEFT=0,
    BOTTOM_RIGHT=1,
    TOP_LEFT=2,
    TOP_RIGHT=3
};

struct TgaHeader{
    int F1; // size: 1 byte | ID Length | 
    int F2; // size: 1 byte | Color Map Type | 
    int F3; // size: 1 byte | Image Type | 
    int F4_1; // size: 2 bytes | First Entry Index
    int F4_2; // size: 2 bytes | Color map Length 
    int F4_3; // size: 1 byte | Color map entry size
    int F5_1; // size: 2 bytes | X-origin of Image
    int F5_2; // size: 2 bytes | Y-origin of Image
    int F5_3; // size: 2 bytes | Image Width
    int F5_4; // size: 2 bytes | Image Height 
    int F5_5; // size: 1 byte | Pixel Depth | Amount of bits per pixel
    int F5_6; // size: 1 byte | Image Descriptor
    std::string F_6; // size: F1 bytes | Title of image
    int F_7; // size: F4_3*F4_2 bytes | Color Map Data. 0 if F2 == 0
    Origin origin;
    int alphaChannel;

    void parse_image_descriptor(){
        int binary[8];
        bin(F5_6, binary);
        int origin_num = binary[2] * 2 + binary[3];
        switch(origin_num){
            case 0 : origin = BOTTOM_LEFT; break;
            case 1 : origin = BOTTOM_RIGHT; break;
            case 2 : origin = TOP_LEFT; break;
            case 3 : origin = TOP_RIGHT; break;
        }
        alphaChannel = binary[4] * 8 + binary[5] * 4 + binary[6] * 2 + binary[7];
    }

    void print(){
        std::cout << "F1   | ID Length            " << F1 << std::endl;
        std::cout << "F2   | Color Map Type       " << F2 << std::endl;
        std::cout << "F3   | Image Type           " << F3 << std::endl;
        std::cout << "F4_1 | First Entry Index    " << F4_1 << std::endl;
        std::cout << "F4_2 | Color map Length     " << F4_2 << std::endl;
        std::cout << "F4_3 | Color map entry size " << F4_3 << std::endl;
        std::cout << "F5_1 | X-origin of Image    " << F5_1 << std::endl;
        std::cout << "F5_2 | Y-origin of Image    " << F5_2 << std::endl;
        std::cout << "F5_3 | Image Width          " << F5_3 << std::endl;
        std::cout << "F5_4 | Image Height         " << F5_4 << std::endl;
        std::cout << "F5_5 | Pixel Depth          " << F5_5 << std::endl;
        std::cout << "origin                      " << origin << std::endl;
        std::cout << "alphaChannel                " << alphaChannel << std::endl;
    }
};

struct TgaFooter{
    int F28; // size: 4 bytes  | Extension Area Offset
    int F29; // size: 4 bytes  | Developer Directory Offset
    std::string F30; // size: 16 bytes | Signature
    int F31; // size: 1 byte   | Fixed period. Ascii character '.'
    int F32; // size: 1 byte   | Final terminator. Binary zero.
    void print(){
        std::cout << "F28 | Extension Area Offset             " << F28 << std::endl;
        std::cout << "F29 | eveloper Directory Offset         " << F29 << std::endl;
        std::cout << "F30 | Signature                         " << F30 << std::endl;
        std::cout << "F31 | Fixed period. Ascii character '.' " << F31 << std::endl;
        std::cout << "F32 | Final terminator. Binary zero.     " << F32 << std::endl;
    }
};

class TgaParser {
public:
    Pixel* pixels;
    TgaHeader header;
    TgaFooter footer;
    
    TgaParser(std::string filepath){
        this->filepath = filepath;
        parse();
    }

private:
    std::string filepath;

    void parse(){
        char filepath_char_array[this->filepath.length() + 1];
        std::strcpy(filepath_char_array, this->filepath.c_str());
        FILE *file = freopen(filepath_char_array, "rb", stdin);  

        if (!file){
            std::cout << "File not found" << std::endl;
        }
        header.F1 = getchar();
        header.F2 = getchar();
        header.F3 = getchar();
        header.F4_1 = getchar() + getchar() * BYTE_SIZE;
        header.F4_2 = getchar() + getchar() * BYTE_SIZE;
        header.F4_3 = getchar() + getchar() * BYTE_SIZE;
        header.F5_1 = getchar();
        header.F5_2 = getchar() + getchar() * BYTE_SIZE;
        header.F5_3 = getchar() + getchar() * BYTE_SIZE;
        header.F5_4 = getchar() + getchar() * BYTE_SIZE;
        header.F5_5 = getchar();
        header.F5_6 = getchar();
        header.parse_image_descriptor();

        int height = header.F5_4;
        int width = header.F5_3;
        pixels = new Pixel[ width*height];

        for(int row = height-1; row >= 0; row--){
            for(int col = 0; col < width; col++){
                pixels[row*width + col] = Pixel(getchar(), getchar(), getchar());
            }
        }
        footer.F28 = getchar() + getchar() * 2 + getchar() * 4 + getchar() * 8;
        footer.F29 = getchar() + getchar() * 2 + getchar() * 4 + getchar() * 8;
        char signature[16];
        for(int i = 0; i < 16; i ++){
            signature[i] = getchar();
        }
        std::string sig_string(signature, 16);
        footer.F30 = sig_string;
        footer.F31 = getchar();
        footer.F32 = getchar();
    }
};