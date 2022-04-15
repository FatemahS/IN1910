#include <iostream>
#include <vector>
#include <string>
#include <math.h>
#include <stdexcept>

using namespace std;


class ArrayList {

    private:
        int *data;
        int capacity;
        int growth;

    public:
            int size;

        ArrayList() {
            size = 0;
            capacity = 1;
            growth = 2;
            data = new int[capacity];
        }

        int length() {
            return size;
        }

        // 1b) - Adding destructor
        ~ArrayList(){
            delete[] data;
        }

        // 1c) - Growing the list
        void append(int n){
            if (capacity <= size){
                resize();
            }
        }

        // I tilfelle man prøver å legge til i listen, uten at det er plass
        // Method som øker capacity med faktor lik 2
        void resize(){
            capacity = capacity * growth;
            int *new_array = new int[capacity];
            for(int i=0; i<size; i++){
                new_array[i] = data[i];
            }
            delete[] data;
            data = new_array;

        }
        // 1d) - Method for å printe på en linje
        void print(){

            for(int i=0; i<size; i++){
                std::cout << data[i] << ", ";
            }
            std::cout << endl;
        }

        // 1f
        ArrayList(vector<int> vec){

            size = vec.size();
            int exp = ceil(log(size)/log(2));
            capacity = pow(2, exp);
            growth = 2;
            data = new int[capacity];
            for(int i=0; i<size; i++){
                data[i] = vec[i];
            }


        }
        // overloading the square-bracketing operator
        int& operator[](int i){
            if(i<size){
                return data[i];

            }
            else{
                throw range_error("The given index is outside the given range");

            }

        }
        // 1g - setter inn value ved en gitt index
        void insert(int val, int index){

            if(index <= size){

                int n = index;

                while(n<size){
                    data[n+1] = data[n];
                    n++;
                }
                data[index] = val;
            }
            else{
                throw range_error("Index is out of range");
            }
        }
    //Removes the element with the given index from the list
        void remove(int index){

            int n = index;
            while(n < (size-1)){
                data[n] = data[n+1];
            }
        }

    //in addition to removing the element at the index given, also returns the removed element
        int pop(int index){
            int removed_value = data[index];
            remove(index);
            shrink_to_fit();
            return removed_value;
        }

    //pops the last element in the list
        int pop(){
            int last_value = pop(size-1);
            shrink_to_fit();
            return last_value;
        }

        // 1j
        void shrink_to_fit(){
            int closest_exp = ceil(log(size)/log(2));
            capacity = pow(2, closest_exp);

            int *new_data = new int[capacity];
            for(int i=0; i<size; i++){
                new_data[i] = data[i];
            }
            delete[] data;
            data = new_data;

        }

};

bool is_prime(int n){
    bool test = true;
    for(int i=2; i<n; i++){
        if(n%i == 0){
            test = false;
        }
    return test;
    }
};

ArrayList find_primes(){
    ArrayList primes;
    int prime_counter = 0;
    int test = 2;

    while(prime_counter < 10){
        if(is_prime(test) == true){
            primes.append(test);
            prime_counter++;
        }
        test++;
    return primes;
    }


};

int main()
{
    ArrayList a;

    std::cout << a.length() << std::endl;

    return 0;
};
