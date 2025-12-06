import { Component, input } from '@angular/core';

@Component({
  selector: 'app-error-banner',
  imports: [],
  templateUrl: './error-banner.html',
})
export class ErrorBanner {
  errorMessage = input.required<string>();
}
