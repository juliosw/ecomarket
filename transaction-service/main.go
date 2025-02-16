package main

import (
    "database/sql"
    "encoding/json"
    "log"
    "net/http"
    "os"

    _ "github.com/lib/pq"
)

type Transaction struct {
    ID        int     `json:"id"`
    ProductID int     `json:"product_id"`
    BuyerID   int     `json:"buyer_id"`
    Amount    float64 `json:"amount"`
}

var db *sql.DB

func initDB() {
    var err error
    connStr := "user=postgres dbname=ecosystem sslmode=disable password=yourpassword host=postgres"
    db, err = sql.Open("postgres", connStr)
    if err != nil {
        log.Fatal(err)
    }
}

func getTransactions(w http.ResponseWriter, r *http.Request) {
    rows, err := db.Query("SELECT id, product_id, buyer_id, amount FROM transactions")
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }
    defer rows.Close()

    var transactions []Transaction
    for rows.Next() {
        var t Transaction
        if err := rows.Scan(&t.ID, &t.ProductID, &t.BuyerID, &t.Amount); err != nil {
            http.Error(w, err.Error(), http.StatusInternalServerError)
            return
        }
        transactions = append(transactions, t)
    }

    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(transactions)
}

func main() {
    initDB()
    http.HandleFunc("/transactions", getTransactions)

    port := os.Getenv("PORT")
    if port == "" {
        port = "8081"
    }

    log.Printf("Transaction Service listening on port %s...", port)
    log.Fatal(http.ListenAndServe(":"+port, nil))
}