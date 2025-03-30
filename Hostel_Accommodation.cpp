#include <bits/stdc++.h>
#include <windows.h>
using namespace std;

class student
{
private:
    string Name, Roll, Address;

public:
    student() : Name(""), Roll(""), Address("") {}
    student(string name, string roll, string addr) : Name(name), Roll(roll), Address(addr) {}

    void setname(string name) { Name = name; }
    void setroll(string roll) { Roll = roll; }
    void setaddress(string addr) { Address = addr; }

    string getName() { return Name; }
    string getRoll() { return Roll; }
    string getaddr() { return Address; }

    void display()
    {
        cout << "\nName: " << Name;
        cout << "\nRoll: " << Roll;
        cout << "\nAddress: " << Address << endl;
    }
};

class Hostel
{
private:
    string name;
    int rent, bed;
    vector<student> students; // Store students in memory

public:
    Hostel(string name, int rent, int bed) : name(name), rent(rent), bed(bed) {}

    string getname() { return name; }
    int getrent() { return rent; }
    int getbed() { return bed; }

    void reserve(string name, string roll, string address)
    {
        if (bed > 0)
        {
            students.push_back(student(name, roll, address));
            bed--;
            cout << "\nReservation successful! Remaining beds: " << bed << endl;
        }
        else
        {
            cout << "\nNo available beds!" << endl;
        }
    }

    void showStd()
    {
        if (students.empty())
        {
            cout << "\nNo students have reserved a bed yet." << endl;
            return;
        }
        cout << "\nList of students in " << name << ":\n";
        for (auto &s : students)
        {
            s.display();
        }
    }
};

int main()
{
    Hostel h("3 Star", 500, 3); // Example: 3 beds available

    bool exit = false;
    while (!exit)
    {
        system("cls");
        int val;
        cout << "\tWelcome to the Hostel Accommodation System" << endl;
        cout << "\t********************************************" << endl;
        cout << "\t1. Reserve A Bed." << endl;
        cout << "\t2. Show All Students" << endl;
        cout << "\t3. Exit." << endl;
        cout << "\tEnter Choice: ";
        cin >> val;

        switch (val)
        {
        case 1:
            system("cls");
            {
                string name, roll, address;
                cin.ignore();
                cout << "\tEnter Name of Student: ";
                getline(cin, name);

                cout << "\tEnter Roll of Student: ";
                getline(cin, roll);

                cout << "\tEnter Address of Student: ";
                getline(cin, address);

                h.reserve(name, roll, address);
                system("pause");
            }
            break;

        case 2:
            system("cls");
            h.showStd();
            system("pause");
            break;

        case 3:
            exit = true;
            break;

        default:
            cout << "\tInvalid Choice! Try Again." << endl;
            system("pause");
            break;
        }
    }

    return 0;
}
