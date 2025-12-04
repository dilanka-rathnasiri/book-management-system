import { HttpClient } from '@angular/common/http';
import { Injectable, Signal, signal, WritableSignal } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class AuthServices {
  bearerToken: WritableSignal<string> = signal('');

  constructor(private httpClient: HttpClient) {}

  validateToken(token: string) {
    const headers = {
      Authorization: `Bearer ${token}`,
    };

    return this.httpClient.get('http://localhost:8000/auth/validate', { headers });
  }

  setToken(token: string): void {
    this.bearerToken.set(token);
  }

  getToken(): Signal<string> {
    return this.bearerToken.asReadonly();
  }
}
