# Sev2:Fired Application Insights Log [SEV-2] ChangeGuard Critical Event requires attention !!

## Overview

This is a generic `catch-all` exception. 
It is used to trigger all exception not caught by the specific exceptions:
- [ChangeGuard - The SSL connection could not be established](SSLConnectionNotEstablished.md).
- [ChangeGuard - Connection refused](ConnectionRefused.md).
- [ChangeGuard - Resource temporarily unavailable](ResourceTemporarilyUnavailable.md).
- [ChangeGuard - CXP Retrieval Error](CXPRetrievalError.md).

#### Use the steps provided in the above TSGs to investigate the problem:
- If the problem falls into one of the previous TSGs, use the steps presented there to mitigate it `and` contact the SME to update that specific Alarm to also catch this kind of exception.
- If the problem is different and can not be investigated using the previous TSGs, contact the SME to look into it and create a new TSG for this specific case.


