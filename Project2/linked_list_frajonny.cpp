#include <iostream>
#include <vector>

using namespace std;

struct Node {
    int value;
    Node *next;
    Node *prev;

    //Two constructor for with or without next and previous pointers.
    Node(int n) {
    value = n;
    next = nullptr;
    prev = nullptr;
}
    Node(int n, Node *p, Node *q) {
    value = n;
    next = p;
    prev = q;
    }
};


class LinkedList {
    private:
        Node *head;
        Node *tail;
        int size;
    //Get node made inside of Private to prevent accecc from outside of class
    //Getting the Node from linked list for given index
        Node* get_node(int index) {
            if (index < 0 or index >= size) {
                throw range_error("IndexError: Index out of range");
            }
            Node* current = head;
            for (int i=0; i<index; i++) {
                current = current->next;
            }
            return current;
        }


    public:
        LinkedList(){
            size = 0;
            head = nullptr;
            tail = nullptr;
        }
        //Constructer for initializing the linked list with given vector.
        LinkedList(vector<int> vec) {
            size = 0;
            head = nullptr;
            tail = nullptr;
            for (int i = 0; i < vec.size(); i++){
                //appending each value in vector in to linked list using append method of ours.
                append(vec[i]);
            }
        }

        int lenght(){
            return size;
        }

        void append(int val) {
            //If list is empty:
            if (head == nullptr) {
                head = new Node(val, nullptr, nullptr);
                size += 1;
                return;
            }

            // Iterate to end of list
            Node* current;
            current = head;
            while (current->next != nullptr) {
                current = current->next;
            }
            // Link new node to end of list
            current->next = new Node(val, nullptr, nullptr);
            size += 1;
            }

        void print() {
            //printing each value in list
            Node* current = head;
            cout << "[";
            while (current->next != nullptr) {
                cout << current->value;
                cout << ", ";
                current = current->next;
            }
            cout << current->value << "]" << endl;
        }

        ~LinkedList() {
            //deleting to save memory
            Node* current;
            Node* next;
            current = head;
            while (current != nullptr) {
                next = current->next;
                delete current;
                current = next;
            }
        }

        int& operator[](int index) {
            return get_node(index)->value;
        }

        void insert(int val, int index) {
            //Here we are able to insert a value in given index for the list
            if (index == 0) {
              Node* next = get_node(index);
              head = new Node(val, next, nullptr);
              size += 1;
              return;
            }
            Node* prev = get_node(index-1);
            Node* next = prev->next;
            prev->next = new Node(val, next, prev);
            size += 1;
        }

        //Remove given index from the list
        void remove(int index) {
          Node* prev = get_node(index-1);
          Node* current = get_node(index);
          if (current->next == nullptr) {
            delete current;
            prev->next = nullptr;
            size -= 1;
            return;
          }
          delete current;
          prev->next = get_node(index+1);
          size -= 1;
        }

        int pop(int index){
            int tmp;
            tmp = get_node(index)->value;
            remove(index);
            return tmp;
        }

        int pop(){
            int tmp;
            tmp = get_node(size-1)->value;
            remove(size-1);
            return tmp;
        }
};


int main() {
    LinkedList a;

    cout << "We start off by appending 2, 4, 6, 8 to the empty list" << endl;
    a.append(2);
    a.append(4);
    a.append(6);
    a.append(8);
    cout << "The current list: ";
    a.print();
    cout << "Length of the list: ";
    cout << a.lenght() << endl;

    cout << "Adding 7 into the list index 0" << endl;
    a.insert(7, 0);

    cout << "The current list: ";
    a.print();

    cout << "Length of the list: ";
    cout << a.lenght() << endl << endl;

    cout << "Removing list index 2";
    a.remove(2);
    cout << "The current list: ";
    a.print();
    cout << "Length of the list: ";
    cout << a.lenght() << endl << endl;


    cout << "Pop index 2 from the list: " << a.pop(2) <<endl;
    cout << "List: ";
    a.print();

    cout << "Pop last index from the list: " << a.pop() <<endl;
    cout << "List: ";
    a.print();
    cout << "Length of the list: " <<a.lenght() <<endl << endl;

    LinkedList b({1,2,3});
    cout << "Making a vector {1, 2, 3} to initialize the linked list" << endl;
    cout << "The List when we start with initializing: ";
    b.print();

    return 0;
}
