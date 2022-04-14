#include <iostream>
#include <vector>
#include <stdexcept>

using namespace std;


struct Node{
    int data;
    Node* next;
    Node* prev;

    Node(int n){
        data = n;
        next = nullptr;
        prev = nullptr;
    }

};



class CircLinkedList{
    private:
        Node* head;
        int size;

    public:
        CircLinkedList(){
            head = nullptr;
            size=0;
        }

        CircLinkedList(int n){
            head = nullptr;
            size = 0;

            // bruker append til å lage en liste
            for(int i=1; i<=n; i++){
                append(i);
            }
        }

        // legger til append
        void append(int val){
            if(head==nullptr){
                head = new Node(val);
                head->next = head;
                head->prev = head;
            }else{
                 Node* temp = new Node(val);

            head->prev->next=temp;
            temp->prev=head->prev;
            head->prev=temp;
            temp->next=head;

            }
            size += 1;
        }

        // 4b
        int&operator[](int index){
            if(size <= 0){
                throw out_of_range("List is empty");
            }
            while(index >= size){
                index -= size;
            }
            Node* current = head;
            for(int i = 0; i<index;i++){
                current = current->next;
            }
            return current->data;
        }

        // 4c - pretty printing
        void print(){
            if(size <= 0){
                throw out_of_range("List is empty");
            }
            Node* current=head;
            cout<<"[";
            for(int i=0; i < size-1;i++){
                cout<<current->data<<", ";
                current=current->next;
            }
            cout<<current->data<<"]"<<endl;
        }

        //Josephus problem

        vector<int> josephus_sequence(int k){
            vector<int> vec_killed;
            Node* current=head;

            int count = 1;

            while(size > 0){
                count++;
                current = current->next;
                if(count == k){
                    vec_killed.push_back(current->data);
                    current->prev->next=current->next;
                    current->next->prev=current->prev;

                    delete current;
                    count = 0;
                    size --;
                }
            }
            return vec_killed;
        }



        ~CircLinkedList(){
            Node* current=head;
            Node* temp;

            for(int i = 0; i < size; i++){
                temp = current->next;
                delete current;
                current = temp;
            }

        }
};



int last_man_standing(int n, int k){
    CircLinkedList clist(n);
    vector<int> killed = clist.josephus_sequence(k);
    return killed[n-1];
};

int main(){
    //4c
    CircLinkedList clist;
    clist.append(0);
    clist.append(2);
    clist.append(4);
    clist.print();
    cout<<"På index 2 er verdien: "<< clist[2] << endl;

    cout<<"I problemet presentert i oppgaven er det denne personen som overlever:  "<< last_man_standing(68,7)<<endl;

    return 0;
}
