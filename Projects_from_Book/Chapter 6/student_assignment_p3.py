# Project 3: E-Commerce Discount Engine
# Fill in every ________ to complete the program.

print('===== Discount Engine =====')

cart_total = float(input('Cart total ($): '))
membership = input('Membership tier (none/silver/gold/platinum): ').lower().strip()
promo_code = input('Promo code (leave blank if none): ').upper().strip()

print(f'Cart total      : ${cart_total:.2f}')
print(f'Membership      : {membership}')
print(f'Promo code      : {promo_code if ________ else "(none)"}')
print()

# ── Step 1: Membership discount percentage ──────────────────────
# Ternary chain: check each tier in order
if membership == 'platinum':
    mem_disc = 15
________ membership == 'gold':
    mem_disc = 10
________ membership == 'silver':
    mem_disc = 5
________:
    mem_disc = 0

# ── Step 2: Promo code discount ─────────────────────────────────
PROMO_CODES = {'SAVE10': 10, 'FLASH20': 20}
# Use a ternary: look up the code if it exists, otherwise 0
promo_disc = PROMO_CODES[promo_code] ________ promo_code ________ PROMO_CODES ________ 0

# ── Step 3: Best discount (higher of membership vs promo) ───────
best_disc = ________(mem_disc, promo_disc)   # built-in picks the larger value

# Apply the best discount
after_best = cart_total * (1 - best_disc / ________)

# ── Step 4: Bulk discount (extra 5% if cart > $200) ────────────
bulk_saving = after_best * 0.05 ________ cart_total ________ 200 ________ 0
after_bulk  = after_best - bulk_saving

# ── Step 5: Loyalty bonus ($5 off if member AND total > $50) ───
is_member     = membership ________ 'none'   # True if not 'none'
loyalty_bonus = 5 ________ (is_member ________ after_bulk ________ 50) ________ 0

final_total = after_bulk - loyalty_bonus

# ── Print breakdown ─────────────────────────────────────────────
print('--- Discount Breakdown ---')
print(f'Membership disc  : {mem_disc}%')
print(f'Promo disc       : {promo_disc}%')
print(f'Best disc applied: {best_disc}%   (higher of membership vs promo)')
print(f'After best disc  : ${after_best:.2f}')
print(f'Bulk disc (5%)   : ${bulk_saving:.2f}   (cart > $200)' ________ cart_total ________ 200
      ________ f'Bulk disc        : N/A   (cart <= $200)')
print(f'After bulk disc  : ${after_bulk:.2f}')
________ loyalty_bonus:
    print(f'Loyalty bonus    : -${loyalty_bonus:.2f}')
print(f'FINAL TOTAL      : ${final_total:.2f}')
