# DateTime Formatting

FCM uses standard date and time format strings. For example:

**With a DateTime value: 2009-06-15T13:45:30 -> 2009-06-15 13:45:30Z**

**With a DateTimeOffset value: 2009-06-15T13:45:30 -> 2009-06-15 20:45:30Z**

More information can be found [here](https://learn.microsoft.com/en-us/dotnet/standard/base-types/standard-date-and-time-format-strings?redirectedfrom=MSDN)

Information on how to convert the DateTimeOffset object to UTC and output it using the format yyyy-MM-dd HH:mm:ssZ can be found [here](https://learn.microsoft.com/en-us/dotnet/api/system.datetimeoffset.tostring?redirectedfrom=MSDN&view=net-7.0#System_DateTimeOffset_ToString_System_String_)