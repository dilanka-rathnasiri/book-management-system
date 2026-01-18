import { Component, signal, WritableSignal } from '@angular/core';
import { Book } from '../models/Book';
import { DataServices } from '../services/data-services';
import { Spinner } from '../spinner/spinner';
import { ErrorBanner } from '../error-banner/error-banner';
import { AuthServices } from '../services/auth-services';
import { Router } from '@angular/router';

@Component({
    selector: 'app-home',
    imports: [Spinner, ErrorBanner],
    templateUrl: './home.html',
})
export class Home {
    books: WritableSignal<Book[]> = signal<Book[]>([]);
    isLoading: WritableSignal<boolean> = signal<boolean>(true);
    errorMessage: WritableSignal<string> = signal<string>('');

    constructor(
        private dataService: DataServices,
        private authServices: AuthServices,
        private router: Router
    ) {}

    ngOnInit() {
        this.dataService.getData().subscribe({
            next: (data) => {
                this.books.set(data);
                this.isLoading.set(false);
            },
            error: (e) => {
                console.error(e);
                this.errorMessage.set(e.message);
                this.isLoading.set(false);
            },
        });
    }

    logout() {
        this.authServices.logout();
        this.router.navigate(['/login']);
    }
}
