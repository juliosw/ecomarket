package main

import (
    "database/sql"
    "encoding/json"
    "log"
    "net/http"
    "os"

    _ "github.com/lib/pq"
)

type Product struct {
    ID    int     `json:"id"`
    Name  string  `json:"name"`
    Price float64 `json:"price"`
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

func getProducts(w http.ResponseWriter, r *http.Request) {
    rows, err := db.Query("SELECT id, name, price FROM products")
    if err != nil {
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }
    defer rows.Close()

    var products []Product
    for rows.Next() {
        var p Product
        if err := rows.Scan(&p.ID, &p.Name, &p.Price); err != nil {
            http.Error(w, err.Error(), http.StatusInternalServerError)
            return
        }
        products = append(products, p)
    }

    w.Header().Set("Content-Type", "application/json")
    json.NewEncoder(w).Encode(products)
}

func main() {
    initDB()
    http.HandleFunc("/products", getProducts)

    port := os.Getenv("PORT")
    if port == "" {
        port = "8080"
    }

    log.Printf("Product Service listening on port %s...", port)
    log.Fatal(http.ListenAndServe(":"+port, nil))
}