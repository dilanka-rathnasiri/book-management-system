import { Component, signal, Signal, WritableSignal } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthServices } from '../services/auth-services';

@Component({
    selector: 'app-login',
    imports: [CommonModule, FormsModule],
    templateUrl: './login.html',
    styleUrl: './login.scss',
})
export class Login {
    bearerToken: Signal<string> = signal('');
    showAlert: WritableSignal<boolean> = signal(false);
    isSuccess: WritableSignal<boolean> = signal(false);

    constructor(
        private authServices: AuthServices,
        private router: Router
    ) {}

    onLogin() {
        const token = this.bearerToken().trim();

        if (token) {
            this.authServices.validateToken(token).subscribe({
                next: (response) => {
                    console.log('API Response:', response);
                    this.showAlert.set(true);
                    this.isSuccess.set(true);
                    this.authServices.setToken(token);

                    // Navigate to home page after successful login
                    this.router.navigate(['']);
                },
                error: (error) => {
                    console.error('API Error:', error);
                    this.showAlert.set(true);
                    this.isSuccess.set(false);
                },
            });
        } else {
            this.showAlert.set(true);
            this.isSuccess.set(false);
        }
    }
}
