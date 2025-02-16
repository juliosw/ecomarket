// api-gateway/main.go
package main

import (
    "net/http"
    "log"
    "github.com/gorilla/mux"
)

func main() {
    r := mux.NewRouter()
    r.HandleFunc("/products", func(w http.ResponseWriter, r *http.Request) {
        // Rota para o Product Service
        http.Redirect(w, r, "http://product-service:8080/products", http.StatusSeeOther)
    })
    r.HandleFunc("/orders", func(w http.ResponseWriter, r *http.Request) {
        // Rota para o Order Service
        http.Redirect(w, r, "http://order-service:8080/orders", http.StatusSeeOther)
    })

    log.Fatal(http.ListenAndServe(":8080", r))
}