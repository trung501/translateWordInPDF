# translateWordInPDF
*Tính năng :
- Đọc tất cả từ trong file pdf rồi dịch sang tiếng việt . 
- Tạo một từ điển cho máy đọc sách kindle từ google dịch.

*Cách dùng : 
- Copy các file pdf vào folder pdf. 
- Chạy server js để tiến hành dùng bing translate ( node app.js) . Trước khi chạy cần cài bing-translate-api qua câu lệnh npm install bing-translate-api.
- Chạy File main.py để tiến hành translate, dữ liệu transtlate được lưu ở tệp dict.npy
- Chạy file writeDictToCSV.py để tiến hành ghi dict.npy sang csv
- Chạy scirpt CsvToMobi.ps1 để chuyển csv sang các định dạng như mobi để sử dụng trên kindle:

