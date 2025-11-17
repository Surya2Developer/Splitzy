// Centralized currency formatting utility
// Default currency: EUR

console.log("✅ currency.js is loaded successfully");

const DEFAULT_CURRENCY_SYMBOL = "€"; // EUR

export function getCurrencySymbol() {
  return DEFAULT_CURRENCY_SYMBOL;
}

export function formatCurrency(amount) {
  if (amount == null || isNaN(Number(amount))) return `${DEFAULT_CURRENCY_SYMBOL}0.00`;
  const num = Number(amount);
  if (!Number.isFinite(num)) return `${DEFAULT_CURRENCY_SYMBOL}0.00`;

  // Format with comma as thousands separator
  return `${DEFAULT_CURRENCY_SYMBOL}${num.toLocaleString(undefined, {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  })}`;
}

// Optional default export (if you want)
export default {
  getCurrencySymbol,
  formatCurrency,
};
