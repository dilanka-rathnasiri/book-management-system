import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
    providedIn: 'root',
})
export class DataServices {
    constructor(private http: HttpClient) {}

    getData(): Observable<any> {
        return this.http.get('http://localhost:8000/books');
    }
}
