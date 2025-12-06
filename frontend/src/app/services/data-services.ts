import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthServices } from './auth-services';

@Injectable({
  providedIn: 'root',
})
export class DataServices {
  constructor(
    private http: HttpClient,
    private authServices: AuthServices,
  ) {}

  getData(): Observable<any> {
    const headers = new HttpHeaders({
      Authorization: `Bearer ${this.authServices.getToken()()}`,
    });

    return this.http.get('http://localhost:8000/books', { headers });
  }
}
