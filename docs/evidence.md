# Evidence & Reproduction Steps

## 1. Login Flow Analysis
- **Finding:** Example — password reset endpoint reveals user existence.
- **Proof-of-Concept:**  
  - Navigate to `/reset`  
  - Enter a non-existent email  
  - Observe response difference between valid vs invalid accounts

## 2. Authentication Boundaries
- **Finding:** Example — weak rate limiting on login attempts.
- **Proof-of-Concept:**  
  - Send multiple invalid login requests  
  - Observe consistent 200/401 responses without throttling

## 3. Session Handling
- **Finding:** Example — JWT not invalidated on logout.
- **Proof-of-Concept:**  
  - Login and capture JWT  
  - Logout  
  - Replay JWT to access protected endpoint

## 4. Authorization & Roles
- **Finding:** Example — IDOR/BOLA vulnerability in workspace records.
- **Proof-of-Concept:**  
  - Authenticated as User A  
  - Access `/api/workspaces/{workspace_id}` belonging to User B  
  - Data returned without authorization check

## 5. API Permission Parity
- **Finding:** Example — API allows direct access to admin endpoints.
- **Proof-of-Concept:**  
  - Call `/api/admin` with normal user token  
  - Observe privileged data/actions exposed

---

## Severity Assessment
- **Critical:** Unauthorized access to tenant/workspace data  
- **High:** Session replay after logout  
- **Medium:** User enumeration via reset endpoint  
- **Low:** Missing rate limits on login

---

## Screenshots / Logs
- Insert safe screenshots or sanitized logs here.
