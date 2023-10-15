package main

import "fmt"

func main() {
	var fname string
	fmt.Print("Enter your first name : ")
	fmt.Scan(&fname)
	fmt.Print("Enter your last name : ")
	var lname string
	fmt.Scan(&lname)
	fmt.Print("Your Full Name is " + fname + " " + lname)

}
