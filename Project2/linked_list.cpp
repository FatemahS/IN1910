#include <string>
#include <iostream>
#include <vector>   //For å ikke få template-error når vi bruker <vector>
using namespace std;


//Task 2a
struct Node {
    int value;
    Node* next;     // Node-pointer to the next node in the list
    Node* prev;     // Node-pointer to the previous node in the list

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

//Task 2b
class LinkedList {
  private:           //Local node-pointers
    Node *head;
    Node *tail;
    int size;

    Node* get_node(int index) {
      if (index < 0 or index >= size) {
        throw range_error("Index out of range");
      }
      Node* current = head;
      for (int i=0; i<index; i++) {
        current = current->next;
      }
      return current;
    }

  public:            //Global
    LinkedList() {   //Constructor
        head = nullptr;
        tail = nullptr;
        size = 0;
      }
      LinkedList(vector<int> vec) {
        head = nullptr;
        tail = nullptr;
        size = 0;
        for (int i = 0; i < vec.size(); i++){
            append(vec[i]);
        }
      }


    int lenght() {
        return size;
    }

    // 2c - append (basert på eksempel fra forelesning)
    void append(int value){
      if (head == nullptr){
          head = new Node(value, nullptr, nullptr);
          size++;
          return;
      }
      Node* current;
      current = head;
      while (current -> next != nullptr){
          current = current -> next;
      }
      current -> next = new Node(value, nullptr, nullptr);
      size++;
    }

    // 2c - print
    void print() {
      Node* current = head;
      cout << "[";
      while (current->next != nullptr) {
          cout << current->value;
          cout << ", ";
          current = current->next;
      }
        cout << current->value << "]" << endl;
    }

    // 2c - destroying the list (basert på eksempel fra forelesning)
    // og tilbakemelding fra forsøk 1
    ~LinkedList() {
      Node* current;
      Node* next;
      current = head;
      while (current != nullptr) {
          next = current->next;
          delete current;
          current = next;
      }
    }

    // 2c - int& operator
    int& operator[](int index) {
        return get_node(index)->value;
      }

    // 2c - sette inn value ved en gitt index
    void insert(int value, int index) {
      if (index == 0) {
        Node* next = get_node(index);
        head = new Node(value, next, nullptr);
        size++;
        return;
      }
      Node* prev = get_node(index-1);
      Node* next = prev->next;
      prev->next = new Node(value, next, prev);
      size++; //holder styr på størrelsen
    }

    void remove(int index) {
      Node* prev = get_node(index-1);
      Node* current = get_node(index);
      if (current->next == nullptr) {
        delete current;
        prev->next = nullptr;
        size --;
        return;
        }
      delete current;
      prev->next = get_node(index+1);
      size --;
    }

    int pop(int index){
      int removed_value;
      removed_value = get_node(index)-> value;
      remove(index); // bruker methoden over
      return removed_value;
    }

    int pop(){
        int removed_value;
        removed_value = get_node(size-1)->value;
        remove(size-1);
        return removed_value;
    }
};

//2d
int main() {
    LinkedList list1;

    //Testing the class
    cout << "Legger til 2, 3, 4 og 5 til den tomme lista ved å bruke append, og får følgende liste:" << endl;
    list1.append(2);
    list1.append(3);
    list1.append(4);
    list1.append(5);
    list1.print();

    cout << "Bruker insert til å legge til 1 på index 0 i lista, og får følgende liste" << endl;
    list1.insert(1, 0);
    list1.print();

    cout << "Bruker remove til å ta vekk elementet med index 3, altså tallet 4, og har nå følgende liste:" << endl;
    list1.remove(3);
    list1.print();

    cout << "Bruker pop til fjerne siste element i lista, og får følgende liste:" << list1.pop() <<endl;
    list1.print();

    cout << "Listens lengde er nå: "  <<endl
    <<list1.lenght()<< endl;

    return 0;
}
