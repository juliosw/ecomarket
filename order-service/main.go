// order-service/main.go
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

func createOrder(w http.ResponseWriter, r *http.Request) {
    // Simulação de criação de pedido
    w.WriteHeader(http.StatusOK)
    w.Write([]byte("Order created"))
}

func main() {
    initDB()
    r := mux.NewRouter()
    r.HandleFunc("/orders", createOrder).Methods("POST")

    log.Fatal(http.ListenAndServe(":8080", r))
}