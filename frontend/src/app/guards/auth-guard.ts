import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthServices } from '../services/auth-services';

export const authGuard: CanActivateFn = (route, state) => {
  const router = inject(Router);
  const authService = inject(AuthServices);
  const token = authService.getToken()();

  if (!token || token.trim() === '') {
    router.navigate(['/login']);
    return false;
  }
  return true;
};
