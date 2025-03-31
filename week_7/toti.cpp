#include <iostream>
#include <vector>
using namespace std;
int main(){
    int n; cin >> n;
    vector<int> songs(n);
    for(int i =0; i<n; i++){
        cin >> songs[i];
    }
    unsigned long long good_combinations = 0; //1X2X
    unsigned long long bad_combinations = 0; //1X
    unsigned long long three_count = count(songs.begin(), songs.end(), 3);
    unsigned long long sum = 0;
    const int MOD = 1000000007;

    for (int i =0; i < n; i++){
        if (songs[i] ==1){
            bad_combinations++;
        }
        else if (songs[i] ==2){
            good_combinations = (2*good_combinations+bad_combinations)%MOD;
            bad_combinations = 0;
            sum += (good_combinations * three_count) % MOD;
            sum %= MOD;
        }
        else if (songs[i] ==3){
            three_count--;
        }
    }
    cout << sum << endl;
    return 0;

}