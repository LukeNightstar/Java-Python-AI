package org.eclipse.java_web.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.MediaType;
import org.springframework.http.client.MultipartBodyBuilder;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.reactive.function.BodyInserters;
import org.springframework.web.reactive.function.client.WebClient;

@RestController
public class RestReqController {

	@Autowired
	private WebClient webClient;
	
	@PostMapping("/java_service")
	public String serviceRequest(MultipartFile file, String message) {
		MultipartBodyBuilder bodyBuilder = new MultipartBodyBuilder(); // 멀티파트 폼 데이터를 구성
		bodyBuilder.part("message", message); // 폼 데이터
		bodyBuilder.part("file", file.getResource()); // 폼 데이터, 파일
        // POST 방식으로 요청. 엔드포인트는 /detect
        // 파일이 전송되므로
        // 폼 데이터를 요청 본문으로 설정
        // 요청을 실행하고 응답을 받음
        // 본문을 String 타입으로 변환
        // 비동기처리를 동기적으로 블록해서 결과를 반환
        return webClient.post().uri("/detect") // POST 방식으로 요청. 엔드포인트는 /detect
                .contentType(MediaType.MULTIPART_FORM_DATA) // 파일이 전송되므로
                .body(BodyInserters.fromMultipartData(bodyBuilder.build())) // 폼 데이터를 요청 본문으로 설정
                .retrieve() // 요청을 실행하고 응답을 받음
                .bodyToMono(String.class) // 본문을 String 타입으로 변환
                .block();
	}
}
