# Phân tích ba dự án CNTT nguồn mở với ba giấy phép khác nhau

## 1. Phạm vi và phương pháp
Bài tập chọn ba dự án có giấy phép khác nhau: GNU Bash (GPL-3.0-or-later), React (MIT) và Apache Spark (Apache-2.0). Phân tích dựa trên trang dự án, tệp LICENSE và hướng dẫn chính thức của tổ chức cấp phép. Cần phân biệt giấy phép của dự án chính với giấy phép của các thư viện/thành phần phụ thuộc đi kèm; một dự án lớn có thể phân phối thành phần của bên thứ ba theo điều kiện khác.

## 2. Ba dự án được lựa chọn

### 2.1 GNU Bash – GPL-3.0-or-later
- **Mục tiêu/phạm vi:** Bash là trình thông dịch lệnh (shell) tương thích sh, được dùng làm giao diện dòng lệnh và ngôn ngữ kịch bản trong hệ thống Unix-like.
- **Giấy phép:** GNU xác nhận Bash được phân phối theo GNU GPL phiên bản 3 hoặc (tùy chọn) bất kỳ phiên bản mới hơn.
- **Cộng đồng:** Dự án thuộc hệ sinh thái GNU/FSF; trang dự án chỉ tới trang phát triển trên Savannah, thông tin maintainer và mailing list. Mô hình cộng tác qua mã nguồn, báo lỗi và bản vá.
- **Điều kiện cốt lõi:** Người dùng được chạy, nghiên cứu, sửa đổi và phân phối. Khi phân phối bản sao hoặc tác phẩm phái sinh thuộc phạm vi GPL, phải cung cấp mã nguồn tương ứng theo điều kiện GPL, giữ thông báo bản quyền/giấy phép và cấp quyền tiếp tục theo GPL. Không được đặt thêm hạn chế làm mất các quyền mà GPL trao.
- **Thương mại/tích hợp:** Có thể sử dụng và bán sản phẩm/dịch vụ liên quan; GPL không cấm thương mại. Tuy nhiên, nếu phân phối một chương trình kết hợp thuộc phạm vi tác phẩm phái sinh GPL, nghĩa vụ copyleft có thể ảnh hưởng đến việc phát hành mã nguồn. Việc chỉ giao tiếp qua tiến trình/giao thức độc lập cần đánh giá theo cấu trúc kỹ thuật và tư vấn pháp lý khi cần.

### 2.2 React – MIT License
- **Mục tiêu/phạm vi:** React là thư viện xây dựng giao diện người dùng cho web và native.
- **Giấy phép:** Repository chính thức ghi nhận React dùng MIT License.
- **Cộng đồng:** Repository công khai trên GitHub, có hướng dẫn đóng góp, quy tắc ứng xử, issues và pull requests; hệ sinh thái phát triển rộng với tài liệu và công cụ bổ trợ.
- **Điều kiện cốt lõi:** MIT cho phép sử dụng, sao chép, sửa đổi, hợp nhất, xuất bản, phân phối, cấp phép lại và bán bản sao; điều kiện chính là giữ thông báo bản quyền và nội dung giấy phép trong các bản sao hoặc phần đáng kể. Phần mềm được cung cấp “as is”, không kèm bảo đảm.
- **Thương mại/tích hợp:** Dễ tích hợp vào sản phẩm đóng và dịch vụ thương mại vì không có nghĩa vụ copyleft buộc công bố mã nguồn của sản phẩm kết hợp chỉ do sử dụng React. Vẫn phải giữ thông báo giấy phép và kiểm tra giấy phép của dependencies, fonts, icons, templates và mã nguồn khác.

### 2.3 Apache Spark – Apache License 2.0
- **Mục tiêu/phạm vi:** Apache Spark là engine phân tích hợp nhất, xử lý dữ liệu quy mô lớn; hỗ trợ các workload như SQL, streaming, machine learning và xử lý đồ thị.
- **Giấy phép:** Repository Apache Spark sử dụng Apache License 2.0.
- **Cộng đồng:** Dự án thuộc Apache Software Foundation (ASF), phát triển theo mô hình cộng đồng mở, có hướng dẫn đóng góp, mailing lists, issue tracking và quy trình phát hành.
- **Điều kiện cốt lõi:** Apache-2.0 cho phép sử dụng, sửa đổi, phân phối và cấp phép lại; khi phân phối cần cung cấp bản sao giấy phép, giữ thông báo bản quyền/patent/trademark/attribution phù hợp, đánh dấu các tệp đã sửa đổi và xử lý tệp NOTICE nếu có. Giấy phép có điều khoản cấp quyền sáng chế từ contributor và cơ chế chấm dứt quyền sáng chế khi khởi kiện liên quan.
- **Thương mại/tích hợp:** Phù hợp với tích hợp vào sản phẩm thương mại và sản phẩm đóng. Không yêu cầu mở toàn bộ mã nguồn sản phẩm kết hợp, nhưng các điều kiện về LICENSE, NOTICE, thông báo thay đổi và giấy phép của thành phần phụ thuộc vẫn phải được tuân thủ.

## 3. So sánh

| Tiêu chí | GNU Bash – GPL-3.0-or-later | React – MIT | Apache Spark – Apache-2.0 |
|---|---|---|---|
| Sử dụng | Tự do, kể cả thương mại | Tự do, kể cả thương mại | Tự do, kể cả thương mại |
| Sửa đổi | Được phép; khi phân phối bản phái sinh phải tuân thủ copyleft | Được phép; giữ thông báo giấy phép | Được phép; đánh dấu thay đổi và giữ thông báo phù hợp |
| Phân phối | Cung cấp mã nguồn tương ứng theo điều kiện GPL khi thuộc phạm vi áp dụng | Giữ copyright và license text | Kèm LICENSE, giữ NOTICE/attribution, ghi nhận thay đổi |
| Copyleft | Mạnh (strong copyleft) | Không | Không |
| Bằng sáng chế | Không có grant sáng chế rõ ràng theo cấu trúc như Apache-2.0 | Không có grant sáng chế rõ ràng trong văn bản MIT | Có grant sáng chế rõ ràng và điều khoản chấm dứt |
| Tích hợp sản phẩm đóng | Rủi ro nghĩa vụ chia sẻ mã nguồn nếu tác phẩm kết hợp thuộc phạm vi GPL | Thường thuận lợi; giữ thông báo | Thường thuận lợi; tuân thủ NOTICE và các điều kiện phân phối |
| Mức độ đơn giản | Điều kiện phân phối phức tạp hơn | Rất ngắn, đơn giản | Chi tiết hơn MIT, đặc biệt về sáng chế và NOTICE |

## 4. Tác động tới cộng đồng và mô hình kinh doanh
GPL tạo cơ chế bảo đảm các bản phân phối phái sinh tiếp tục duy trì quyền tự do phần mềm; đổi lại, doanh nghiệp phải thiết kế ranh giới tích hợp và quy trình tuân thủ cẩn thận. MIT giảm rào cản tái sử dụng, thuận lợi cho thư viện nền tảng, hệ sinh thái framework và doanh nghiệp muốn kết hợp với mã nguồn đóng. Apache-2.0 cũng thân thiện với thương mại nhưng bổ sung cơ chế cấp quyền sáng chế và yêu cầu thông báo rõ ràng, phù hợp với các dự án hạ tầng lớn có nhiều tổ chức tham gia.

## 5. Nhận xét và lựa chọn giấy phép
- **Dự án muốn bảo đảm phần mềm phái sinh được duy trì mở:** GPL-3.0-or-later phù hợp, với điều kiện nhóm phát triển chấp nhận nghĩa vụ copyleft khi phân phối.
- **Thư viện nhỏ, ví dụ học tập hoặc component muốn được tái sử dụng rộng:** MIT phù hợp nhờ văn bản ngắn, dễ hiểu và ít ràng buộc.
- **Nền tảng/hạ tầng doanh nghiệp, cộng tác đa tổ chức và quan tâm đến sáng chế:** Apache-2.0 là lựa chọn cân bằng giữa khả năng tái sử dụng thương mại, minh bạch thông báo và bảo vệ sáng chế.

Không có giấy phép “tốt nhất” cho mọi trường hợp. Việc lựa chọn phụ thuộc mục tiêu duy trì tính mở, mô hình doanh thu, cách phân phối, cấu trúc liên kết/tích hợp và mức độ chấp nhận nghĩa vụ tuân thủ. Đây là phân tích học thuật, không thay thế tư vấn pháp lý.

## 6. Kết luận
Ba giấy phép thể hiện ba triết lý khác nhau: GPL ưu tiên bảo đảm tự do cho các bản phái sinh; MIT ưu tiên đơn giản và khả năng tái sử dụng; Apache-2.0 kết hợp quyền sử dụng rộng với điều khoản sáng chế và thông báo phân phối. Khi sử dụng mã nguồn mở trong sản phẩm thực tế, tổ chức cần lập danh mục thành phần (SBOM), lưu bản giấy phép, theo dõi NOTICE, ghi nhận thay đổi và rà soát license của toàn bộ dependencies.
