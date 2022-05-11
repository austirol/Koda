
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "naloga.h"

int poisciStudenta(Student** studentje, int stStudentov, int vpisna) {
    // popravite / dopolnite ...
    int indeks = -1;
    for (int i = 0; i < stStudentov; i++) {
        if (studentje[i]->vpisna == vpisna) {
            indeks = i;
            break;
        }
    }
    return indeks;
}

int poisciPO(Student* student, char* predmet) {
    // popravite / dopolnite ...
    for (int i = 0;i < student->stPO;i++) {
        if (strcmp(student->po[i].predmet, predmet) == 0) return i;
    }
    return -1;
}

int dodaj(Student** studentje, int stStudentov, int vpisna, char* predmet, int ocena) {
    // popravite / dopolnite ...
    int poSt = poisciStudenta(studentje, stStudentov, vpisna);
    //student ne obstaja
    if (poSt == -1) {
        Student *student = calloc(1, sizeof(Student));
        student->po = calloc(10, sizeof(PO));
        student->stPO = 0;
        student->vpisna = vpisna;
        studentje[stStudentov] = student;
        stStudentov++;
    }
    poSt = poisciStudenta(studentje, stStudentov, vpisna);
    //printf("-%d\n", poSt);
    if (poSt != -1) {
    //student obstaja
        int poPo = poisciPO(studentje[poSt], predmet);
        //printf("+%d\n",poPo);
        //predmet obstaja
        if (poPo != -1) {
            //printf("!%d\n",studentje[poSt]->po[poPo].ocena);
            studentje[poSt]->po[poPo].ocena = ocena;
            return stStudentov;
        } else {
            for (int i = 0; i < 4; i++) {
                studentje[poSt]->po[(studentje[poSt]->stPO)].predmet[i] = predmet[i];
            }
            studentje[poSt]->po[(studentje[poSt]->stPO)].ocena = ocena;
            studentje[poSt]->stPO++;
            return stStudentov;
        }
    }
    return stStudentov;
}



int main() {
    // koda za ro"cno testiranje (po "zelji)


    return 0;
}
