// product-service/main.go
package main

import (
    "database/sql"
    "fmt"
    "log"
    "net/http"
    "os"
    "github.com/gorilla/mux"
    _ "github.com/lib/pq"
)

var db *sql.DB

func initDB() {
    var err error
    connStr := fmt.Sprintf("user=%s dbname=%s sslmode=disable password=%s host=%s",
        os.Getenv("POSTGRES_USER"),
        os.Getenv("POSTGRES_DB"),
        os.Getenv("POSTGRES_PASSWORD"),
        os.Getenv("POSTGRES_HOST"),
    )
    db, err = sql.Open("postgres", connStr)
    if err != nil {
        log.Fatal(err)
    }
}

func getProducts(w http.ResponseWriter, r *http.Request) {
    rows, err := db.Query("SELECT id, name, price FROM products")
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }
    defer rows.Close()

    var products []string
    for rows.Next() {
        var id int
        var name string
        var price float64
        if err := rows.Scan(&id, &name, &price); err != nil {
            http.Error(w, err.Error(), http.StatusInternalServerError)
            return
        }
        products = append(products, fmt.Sprintf("ID: %d, Name: %s, Price: %.2f", id, name, price))
    }

    w.WriteHeader(http.StatusOK)
    w.Write([]byte(fmt.Sprintf("%v", products)))
}

func main() {
    initDB()
    r := mux.NewRouter()
    r.HandleFunc("/products", getProducts).Methods("GET")

    log.Fatal(http.ListenAndServe(":8080", r))
}