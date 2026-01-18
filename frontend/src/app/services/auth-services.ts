import { HttpClient } from '@angular/common/http';
import { Injectable, Signal, signal, WritableSignal } from '@angular/core';

@Injectable({
    providedIn: 'root',
})
export class AuthServices {
    private readonly TOKEN_KEY = 'bearerToken';
    bearerToken: WritableSignal<string> = signal('');

    constructor(private httpClient: HttpClient) {
        this.loadToken();
    }

    validateToken(token: string) {
        const headers = {
            Authorization: `Bearer ${token}`,
        };

        return this.httpClient.get('http://localhost:8000/auth/validate', { headers });
    }

    setToken(token: string): void {
        this.bearerToken.set(token);
        sessionStorage.setItem(this.TOKEN_KEY, token);
    }

    getToken(): Signal<string> {
        return this.bearerToken.asReadonly();
    }

    private loadToken(): void {
        const savedToken = sessionStorage.getItem(this.TOKEN_KEY);
        if (savedToken) {
            this.bearerToken.set(savedToken);
        }
    }

    logout(): void {
        this.bearerToken.set('');
        sessionStorage.removeItem(this.TOKEN_KEY);
    }

    isAuthenticated(): boolean {
        if (!this.bearerToken() || this.bearerToken().trim() === '') {
            return false;
        }
        return true;
    }
}
