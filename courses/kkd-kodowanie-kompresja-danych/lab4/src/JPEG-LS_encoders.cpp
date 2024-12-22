#include"Pixel.h"

int modulo(int x, int y){
    int z = x%y;
    if (z >= 0){
        return z;
    }
    else{
        return y + z;
    }
}

int max(int a, int b){
    if (a>=b)
        return a;
    return b;
}
int min(int a, int b){
    if (a<=b)
        return a;
    return b;
}

int new_standard(int NW, int N, int W){
    if (NW >= max(W, N))
        return max(W,N);
    else if (N <= min(W,N))
        return min(W, N);
    else
        return W + N - NW;
        
}

int prediction(int NW, int N, int W, int prediction_index){
    switch(prediction_index){
        case 1: return W; break;
        case 2: return N; break;
        case 3: return NW; break;
        case 4: return N + W - NW; break;
        case 5: return N + (W - NW)/2; break;
        case 6: return W + (N - NW)/2; break;
        case 7: return (N + W)/2; break;
        case 8: return new_standard(NW, N, W); break;
        default: return -1; break;
    }
}

void encode(Pixel* pixels, int height, int width, Pixel* encoded_pixels, int prediction_index){
    for(int row = height-1; row >= 0; row--){
        for(int col = 0; col < width; col++){
            Pixel current = pixels[row*width+col];
            Pixel N = ((row == 0) ? Pixel(0,0,0) : pixels[(row-1)*width + col]);
            Pixel W = ((col == 0) ? Pixel(0,0,0) : pixels[row*width + (col-1)]);
            Pixel NW = ((col == 0 || row == 0) ? Pixel(0,0,0) : pixels[(row-1)*width + (col-1)]);

            int r = modulo(current.r - prediction(NW.r, N.r, W.r, prediction_index), 256);
            int g = modulo(current.g - prediction(NW.g, N.g, W.g, prediction_index), 256);
            int b = modulo(current.b - prediction(NW.b, N.b, W.b, prediction_index), 256);
            encoded_pixels[row*width+col] = Pixel(b, g, r);
        }
    }
}