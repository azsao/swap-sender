#include <Windows.h>
#include <iostream>
#include <string>

// Function prototypes
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);
void ShowNotification(const std::wstring& title, const std::wstring& message);
void ExecutePythonScript();
void ScheduleNotification(HWND hwnd);

// Main function
int WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow);

// Window procedure
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam) {
    switch (uMsg) {
    case WM_CREATE:
        // Run the notification scheduler when the window is created
        ScheduleNotification(hwnd);
        break;
    case WM_DESTROY:
        // Exit the application when the window is destroyed
        PostQuitMessage(0);
        break;
    default:
        return DefWindowProc(hwnd, uMsg, wParam, lParam);
    }
    return 0;
}

// Show notification function
void ShowNotification(const std::wstring& title, const std::wstring& message) {
    MessageBoxW(NULL, message.c_str(), title.c_str(), MB_ICONINFORMATION);
}

// Execute Python script function
void ExecutePythonScript() {
    // Replace with the correct path to your Python script
    system("python execute.py");
}

// Schedule notification function
void ScheduleNotification(HWND hwnd) {
    // Set the time for 18:00 EST
    SYSTEMTIME st;
    GetLocalTime(&st);
    st.wHour = 18;
    st.wMinute = 0;
    st.wSecond = 0;
    st.wMilliseconds = 0;

    FILETIME ft;
    SystemTimeToFileTime(&st, &ft);

    ULARGE_INTEGER ull;
    ull.LowPart = ft.dwLowDateTime;
    ull.HighPart = ft.dwHighDateTime;

    // Create a timer that triggers at the specified time
    HANDLE hTimer = CreateWaitableTimer(NULL, TRUE, NULL);
    SetWaitableTimer(hTimer, (LARGE_INTEGER*)&ull, 0, NULL, NULL, 0);

    // Associate the timer with the window to receive timer messages
    SetTimer(hwnd, 1, 1000, nullptr);

    // Message loop for timer messages
    MSG msg;
    while (GetMessage(&msg, hwnd, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    // Close the timer handle
    CloseHandle(hTimer);
}

// Main function
int WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nCmdShow) {
    // Create a hidden window
    HWND hwnd = CreateWindowExW(0, L"STATIC", L"NotificationApp", 0, 0, 0, 0, 0, HWND_MESSAGE, NULL, hInstance, NULL);

    // Run the notification scheduler
    ScheduleNotification(hwnd);

    // Message loop
    MSG msg;
    while (GetMessage(&msg, nullptr, 0, 0)) {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}
