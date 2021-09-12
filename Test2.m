
function Test2
    clc
    
    function [Q,R]=cgs(A,n)
        for j=1:n
            v=A(:,j);
            for i=1:j-1
                q=Q(:,i);
                R(i,j)=dot(q,A(:,j));
                v=v-q*R(i,j);
            end
            R(j,j)=norm(v);
            Q(:,j)=v/R(j,j);
        end
    end

    function [Q,R]=mgs(A,n)
        V4=A;
        for i=1:n
            R(i,i)=norm(V4(:,i));
            q=V4(:,i)/R(i,i);
            Q(:,i)=q;
            for j=i+1:n
                R(i,j)=dot(q,V4(:,j));
                V4(:,j)=V4(:,j)-q*R(i,j);
            end
        end
     end 

    m=80;
    n=m/2;
    ncy=32;
    [U2,X1]=qr(randn(m));
    U=U2(:,1:n);
    [V,X2]=qr(randn(n));
       
    D(n,n)=0.;
    KX(ncy)=0.;
    ER(ncy)=0.;
    ER_HH(ncy)=0.0;


for kcy=1:ncy
 
    KA=10^kcy;
    AL=log10(KA)/(n-1);
    KX(kcy)=log10(KA);
    ER(kcy)=log10(KX(kcy));

    for i=1:n
        d(i)=10^(AL*(i-1));
        D(i,i)=d(i);
    end

    A=U*D*V';
   
    [QC,RC]=cgs(A,n);
    ER_CGS(kcy)=log10(norm(eye(n)-QC'*QC,'fro'));
    
    [QM,RM]=mgs(A,n);
    ER_MGS(kcy)=log10(norm(eye(n)-QM'*QM,'fro'));
    
    [Q2,R]=qr(A);
    Q=Q2(:,1:n);
    ER_HH(kcy)=log10(norm(eye(n)-Q'*Q,'fro'))
end

    KX;
    ER_CGS;
    ER_MGS;
    ER_HH;
    
    plot(KX,ER_CGS,'r--')
    hold on
    plot(KX,ER_MGS,'g:+')
    hold on
    plot(KX,ER_HH,'b-*')
    xlabel('log10(kA)')
    ylabel('log10(I-QtQ)')
    legend('CGS','MGS','Householder')
    
end
    

