#include<iostream>
#include"TgaParser.cpp"
#include"entropy_calculator.cpp"
#include"JPEG-LS_encoders.cpp"
#include"Pixel.h"

int min_list(double* arr, int n){
    int index = 0;
    double value = arr[0];
    for(int i = 1; i < n; i++){
        if (value > arr[i]){
            index = i;
            value = arr[i];
        }
    }
    return index;
}

void calculate_entropies_for_jpeg_encodings(std::string filename){
    TgaParser parser = TgaParser("../pictures/" + filename); 
    int width = parser.header.F5_3;
    int height = parser.header.F5_4;  

    double a_entropies[9] = {0};
    double b_entropies[9] = {0};
    double g_entropies[9] = {0};
    double r_entropies[9] = {0};  

    b_entropies[0] = entropy(parser.pixels, width, height, "blue");
    g_entropies[0] = entropy(parser.pixels, width, height, "green"); 
    r_entropies[0] = entropy(parser.pixels, width, height, "red"); 
    a_entropies[0] = entropy(parser.pixels, width, height, "all");
     
    for(int pred_index = 1; pred_index <= 8; pred_index++){
        Pixel* encoded_pixels = new Pixel[height*width]; 
        encode(parser.pixels, height, width, encoded_pixels, pred_index);
        
        b_entropies[pred_index] = entropy(encoded_pixels, width, height, "blue"); 
        g_entropies[pred_index] = entropy(encoded_pixels, width, height, "green");  
        r_entropies[pred_index] = entropy(encoded_pixels, width, height, "red");
        a_entropies[pred_index] = entropy(encoded_pixels, width, height, "all"); 
    }

    std::cout << "Entropies for different JPEG-LS_encodings" << std::endl; 
    std::cout << "ID |  RED  | GREEN | BLUE  | ALL " << std::endl;  
    for(int pred_index = 0; pred_index < 9; pred_index++){
        printf("%d  |  %.2f | %.2f  | %.2f  | %.2f\n", pred_index, r_entropies[pred_index], g_entropies[pred_index], b_entropies[pred_index], a_entropies[pred_index]);
    }
    int best_blue = min_list(b_entropies, 9);
    int best_red = min_list(r_entropies, 9);
    int best_green = min_list(g_entropies, 9);
    int best_all = min_list(a_entropies, 9); 
    printf("Best prediction for blue is %d %.2f\n", best_blue, b_entropies[best_blue]);
    printf("Best prediction for red is %d %.2f\n", best_red, r_entropies[best_red]);
    printf("Best prediction for green is %d %.2f\n", best_green, g_entropies[best_green]);
    printf("Best prediction for all is %d %.2f\n", best_all, a_entropies[best_all]);
}

int main( int argc, char **argv ) {
    std::string filename = argv[1];
    calculate_entropies_for_jpeg_encodings(filename);
}