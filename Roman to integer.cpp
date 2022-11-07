class Solution {
public:

    int romanToInt(string s) {
        int num;
        bool proceed;
        int slen;
        slen = s.length();
        if ((slen >= 1) && (slen <= 15)){
            for(int i=0; i<slen; i++){
                switch(s[i]){
                    case 'I' : proceed = true; break;
                    case 'V' : proceed = true; break;
                    case 'X' : proceed = true; break;
                    case 'L' : proceed = true; break;
                    case 'C' : proceed = true; break;
                    case 'D' : proceed = true; break;
                    case 'M' : proceed = true; break;
                    default : proceed = false;
                }
            }
        }
        if(proceed){
            num = 0;
            for(int i=0; i<slen; i++){
                
                switch(s[i]){
                        
                    case 'I' :  num = num + 1;
                                if ((i+1)<slen){
                                    switch(s[i+1]){
                                        case 'V' : num = num + 4 - 1;
                                        i++;
                                        break;
                                        case 'X' : num = num + 9 - 1;
                                        i++;
                                        break;
                                    }
                                }
                                break;
                        
                    case 'X' :  num = num + 10;
                                if ((i+1)<slen){
                                    switch(s[i+1]){
                                        case 'L' : num = num + 40 - 10; 
                                        i++;
                                        break;
                                        case 'C' : num = num + 90 - 10;
                                        i++;
                                        break;
                                    }
                                }
                                break;
                        
                    case 'C' :  num = num + 100;
                                if ((i+1)<slen){
                                    switch(s[i+1]){
                                        case 'D' : num = num + 400 - 100;
                                        i++;
                                        break;
                                        case 'M' : num = num + 900 - 100;
                                        i++;
                                        break;
                                    }
                                }
                                break;
                    case 'V' : num = num + 5; break;
                    case 'L' : num = num + 50; break;
                    case 'D' : num = num + 500; break;
                    case 'M' : num = num + 1000; break;
                }
            }
        }
        return num;
    }
};